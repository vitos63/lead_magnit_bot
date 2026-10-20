import { type ReactNode, useEffect, useState } from 'react'
import { getAnswers, saveAnswer } from './api'
import ContactInput from './ContactInput'
import { type Answer, BOOL_LABELS, type Question } from './questions'
import Toggle from './Toggle'

type Props = {
  questions: Question[]
  url: string
  intro?: ReactNode
  children?: ReactNode
  doneLabel?: string
  canFinish?: boolean
  onDone: () => void | Promise<void>
}

export default function Questionnaire({
  questions,
  url,
  intro,
  children,
  doneLabel = 'Продолжить →',
  canFinish = true,
  onDone,
}: Props) {
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

  const { name, text, type, labels = BOOL_LABELS, placeholder = 'Напишите ваш ответ…' } = questions[index]
  const answer = answers[name]
  const last = index === questions.length - 1
  const setAnswer = (value: Answer) => setAnswers((prev) => ({ ...prev, [name]: value }))

  async function handleNext(value = answer) {
    setSaving(true)
    setError('')
    try {
      await saveAnswer(url, name, value)
      if (last) await onDone()
      else setIndex(index + 1)
    } catch (e) {
      setError((e as Error).message)
    } finally {
      setSaving(false)
    }
  }

  function handleChoice(value: Answer) {
    if (saving) return
    setAnswer(value)
    handleNext(value)
  }

  return (
    <main>
      <div className="progress">
        <span style={{ width: `${((index + 1) / questions.length) * 100}%` }} />
      </div>
      {index === 0 && intro}
      <section key={name} className="card">
        <p className="label">
          Вопрос {index + 1}/{questions.length}
        </p>
        <h1>{text}</h1>
        {type === 'bool' && (
          <Toggle<Answer>
            options={[
              { value: true, label: labels[0] },
              { value: false, label: labels[1] },
            ]}
            value={answer ?? true}
            onChange={handleChoice}
          />
        )}
        {type === 'text' && (
          <textarea placeholder={placeholder} value={String(answer ?? '')} onChange={(e) => setAnswer(e.target.value)} />
        )}
        {type === 'contact' && <ContactInput value={answer} onChange={setAnswer} />}
        {last && children}
        {type !== 'bool' && (
          <button
            className="big"
            disabled={answer === undefined || answer === '' || saving || (last && !canFinish)}
            onClick={() => handleNext()}
          >
            {last ? doneLabel : 'Продолжить →'}
          </button>
        )}
      </section>
      {index > 0 && (
        <button className="back" disabled={saving} onClick={() => setIndex(index - 1)}>
          ← Назад
        </button>
      )}
      {error && <p className="error">Не сохранилось: {error}</p>}
    </main>
  )
}
