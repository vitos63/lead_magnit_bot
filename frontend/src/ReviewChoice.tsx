import { useEffect, useState } from 'react'
import { getResult } from './api'

type Props = {
  onPersonalReview: () => void
  onSkip: () => void
}

export default function ReviewChoice({ onPersonalReview, onSkip }: Props) {
  const [result, setResult] = useState('')

  useEffect(() => {
    getResult()
      .then(setResult)
      .catch(() => {})
  }, [])

  return (
    <main>
      <h1>Результат диагностики</h1>
      {result && <p className="card result">{result}</p>}
      <div className="nav">
        <button className="next" onClick={onPersonalReview}>
          Личный разбор
        </button>
        <button onClick={onSkip}>Пропуск разбора</button>
      </div>
    </main>
  )
}
