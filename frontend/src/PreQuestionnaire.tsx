import { useState } from 'react'
import { sendPreQuestionnaire } from './api'
import { PRE_QUESTIONS } from './questions'
import Questionnaire from './Questionnaire'

export default function PreQuestionnaire({ onSent }: { onSent: () => void }) {
  const [answered, setAnswered] = useState(false)
  const [consent, setConsent] = useState(false)
  const [sending, setSending] = useState(false)
  const [error, setError] = useState('')

  async function handleSend() {
    setSending(true)
    setError('')
    try {
      await sendPreQuestionnaire()
      onSent()
    } catch (e) {
      setError((e as Error).message)
    } finally {
      setSending(false)
    }
  }

  if (!answered) return <Questionnaire questions={PRE_QUESTIONS} url="/pre_questionnaire" onDone={() => setAnswered(true)} />

  return (
    <main>
      <section className="card">
        <label className="consent">
          <input type="checkbox" checked={consent} onChange={(e) => setConsent(e.target.checked)} />
          Я согласен(на) на обработку предоставленных данных для рассмотрения моей заявки и на связь со мной по поводу
          личного разбора.
        </label>
        <button className="big" disabled={!consent || sending} onClick={handleSend}>
          Отправить заявку на разбор →
        </button>
      </section>
      {error && <p className="error">Не отправилось: {error}</p>}
    </main>
  )
}
