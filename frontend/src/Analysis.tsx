import { useEffect, useState } from 'react'
import { getStage, POLL_INTERVAL } from './api'

const TIMEOUT = 180000

export default function Analysis({ onReady }: { onReady: (stage: string) => void }) {
  const [failed, setFailed] = useState(false)

  useEffect(() => {
    const started = Date.now()
    const timer = setInterval(async () => {
      const stage = await getStage().catch(() => 'START')
      if (stage !== 'START') onReady(stage)
      else if (Date.now() - started > TIMEOUT) setFailed(true)
      else return
      clearInterval(timer)
    }, POLL_INTERVAL)
    return () => clearInterval(timer)
  }, [onReady])

  if (failed)
    return (
      <main>
        <h1>Не получилось подготовить разбор</h1>
        <p className="muted">Попробуйте пройти диагностику ещё раз чуть позже.</p>
      </main>
    )

  return (
    <main className="centered">
      <div className="spinner" />
      <h1>AI анализирует ваши ответы</h1>
      <p className="muted">Сопоставляем продукт, оффер, трафик и Telegram.</p>
      <p className="muted">Ищем слабое звено, из-за которого вы можете терять заявки.</p>
    </main>
  )
}
