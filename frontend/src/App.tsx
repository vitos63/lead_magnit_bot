import { useState } from 'react'
import { saveAnswer } from './api'
import { QUESTIONS, type Answer } from './questions'
import { tgId } from './telegram'

export default function App() {
  const [index, setIndex] = useState(0)
  const [answers, setAnswers] = useState<Record<string, Answer>>({})
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')

  if (!tgId) return <p>Откройте форму из Telegram-бота</p>
  if (index === QUESTIONS.length) return <p>Спасибо, ответы сохранены!</p>

  const { name, text, type } = QUESTIONS[index]
  const answer = answers[name]
  const setAnswer = (value: Answer) => setAnswers((prev) => ({ ...prev, [name]: value }))

  async function handleNext() {
    setSaving(true)
    setError('')
    try {
      await saveAnswer(name, answer)
      setIndex(index + 1)
    } catch (e) {
      setError((e as Error).message)
    } finally {
      setSaving(false)
    }
  }

  return (
    <main>
      <div className="progress">
        {QUESTIONS.map((question, i) => (
          <span key={question.name} className={i <= index ? 'done' : ''} />
        ))}
      </div>
      <p className="step">
        Шаг {index + 1} из {QUESTIONS.length}
      </p>
      <h1>{text}</h1>
      {type === 'bool' ? (
        <div className="toggle">
          {[true, false].map((value) => (
            <label key={String(value)} className={answer === value ? 'selected' : ''}>
              <input type="radio" name={name} checked={answer === value} onChange={() => setAnswer(value)} />
              {value ? 'Да' : 'Нет'}
            </label>
          ))}
        </div>
      ) : (
        <textarea value={String(answer ?? '')} onChange={(e) => setAnswer(e.target.value)} />
      )}
      <div className="nav">
        <button disabled={index === 0 || saving} onClick={() => setIndex(index - 1)}>
          Назад
        </button>
        <button className="next" disabled={answer === undefined || answer === '' || saving} onClick={handleNext}>
          {index === QUESTIONS.length - 1 ? 'Готово' : 'Далее'}
        </button>
      </div>
      {error && <p className="error">Не сохранилось: {error}</p>}
    </main>
  )
}
