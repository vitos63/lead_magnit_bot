import { useEffect, useState } from 'react'
import { getAnswers, saveAnswer } from './api'
import ContactInput from './ContactInput'
import type { Answer, Question } from './questions'
import Toggle from './Toggle'

type Props = {
  questions: Question[]
  url: string
  onDone: () => void
}

export default function Questionnaire({ questions, url, onDone }: Props) {
  const [index, setIndex] = useState(0)
  const [answers, setAnswers] = useState<Record<string, Answer> | null>(null)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    getAnswers(url)
      .catch(() => ({}))
      .then((saved) => {
        const unanswered = questions.findIndex((question) => !(question.name in saved))
        setIndex(unanswered === -1 ? questions.length - 1 : unanswered)
        setAnswers(saved)
      })
  }, [questions, url])

  if (!answers) return <p>Загрузка…</p>

  const { name, text, type, labels = ['Да', 'Нет'] } = questions[index]
  const answer = answers[name]
  const setAnswer = (value: Answer) => setAnswers((prev) => ({ ...prev, [name]: value }))
  const isLast = index === questions.length - 1

  async function handleNext() {
    setSaving(true)
    setError('')
    try {
      await saveAnswer(url, name, answer)
      if (isLast) onDone()
      else setIndex(index + 1)
    } catch (e) {
      setError((e as Error).message)
    } finally {
      setSaving(false)
    }
  }

  return (
    <main>
      <div className="progress">
        {questions.map((question, i) => (
          <span key={question.name} className={i <= index ? 'done' : ''} />
        ))}
      </div>
      <p className="step">
        Шаг {index + 1} из {questions.length}
      </p>
      <h1>{text}</h1>
      {type === 'bool' && (
        <Toggle<Answer>
          name={name}
          options={[
            { value: true, label: labels[0] },
            { value: false, label: labels[1] },
          ]}
          value={answer}
          onChange={setAnswer}
        />
      )}
      {type === 'text' && <textarea value={String(answer ?? '')} onChange={(e) => setAnswer(e.target.value)} />}
      {type === 'contact' && <ContactInput value={answer} onChange={setAnswer} />}
      <div className="nav">
        <button disabled={index === 0 || saving} onClick={() => setIndex(index - 1)}>
          Назад
        </button>
        <button className="next" disabled={answer === undefined || answer === '' || saving} onClick={handleNext}>
          {isLast ? 'Готово' : 'Далее'}
        </button>
      </div>
      {error && <p className="error">Не сохранилось: {error}</p>}
    </main>
  )
}
