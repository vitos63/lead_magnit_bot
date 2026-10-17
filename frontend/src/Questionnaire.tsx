import { useState } from 'react'
import { saveAnswer } from './api'
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
  const [answers, setAnswers] = useState<Record<string, Answer>>({})
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')

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
