import { useEffect, useState } from 'react'
import { getResult, type Result } from './api'

type Props = {
  onPersonalReview: () => void
  onSkip: () => void
}

export default function ReviewChoice({ onPersonalReview, onSkip }: Props) {
  const [result, setResult] = useState<Result | null>()

  useEffect(() => {
    getResult()
      .then(setResult)
      .catch(() => setResult(null))
  }, [])

  if (result === undefined) return null

  return (
    <main>
      {result && (
        <section className="card">
          <h1>Ваша система заявок</h1>
          <div className="bars">
            {result.directions.map(({ title, score }) => (
              <div key={title} className={title === result.leak ? 'bar leak' : 'bar'}>
                <span>{title}</span>
                <span>{score}/10</span>
                <div className="progress">
                  <span style={{ width: `${score * 10}%` }} />
                </div>
              </div>
            ))}
          </div>
          <h1>
            Главная утечка — {result.leak} · {result.directions.find(({ title }) => title === result.leak)?.score}/10
          </h1>
          <p className="result">{result.text}</p>
        </section>
      )}
      <button className="big" onClick={onPersonalReview}>
        Хочу личный разбор →
      </button>
      <button className="big secondary" onClick={onSkip}>
        Знаю проблему. Хочу решение →
      </button>
    </main>
  )
}
