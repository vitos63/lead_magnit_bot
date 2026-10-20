import { useEffect, useState } from 'react'
import { type DiagnosticResult, getResult } from './api'

type NextProps = { onNext: () => void }

const BENEFITS = [
  'Более глубокий взгляд на вашу ситуацию',
  'Понимание, что мешает получать больше заявок',
  'Приоритетные шаги для исправления системы',
]

export default function Result({ onPersonalReview }: { onPersonalReview: () => void }) {
  const [result, setResult] = useState<DiagnosticResult | null>()
  const [step, setStep] = useState(0)

  useEffect(() => {
    getResult()
      .then(setResult)
      .catch(() => setResult(null))
  }, [])

  useEffect(() => window.scrollTo(0, 0), [step])

  if (result === undefined) return null

  const next = () => setStep(step + 1)
  const screens = [
    result && <Scores key="scores" result={result} onNext={next} />,
    result && <Diagnosis key="diagnosis" result={result} onNext={next} />,
    <NextStep key="next" onNext={next} />,
    <Invite key="invite" onNext={onPersonalReview} />,
  ].filter(Boolean)

  return (
    <main>
      {screens[step]}
      {step > 0 && (
        <button className="back" onClick={() => setStep(step - 1)}>
          ← Назад
        </button>
      )}
    </main>
  )
}

function Scores({ result, onNext }: NextProps & { result: DiagnosticResult }) {
  return (
    <>
      <section className="card">
        <h1>Ваш результат диагностики</h1>
        <p className="muted">Вот как сейчас работают четыре элемента вашей системы привлечения заявок.</p>
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
      </section>
      <section className="card leak">
        <p className="label">Главная утечка</p>
        <h2>
          {result.leak} — {result.directions.find(({ title }) => title === result.leak)?.score}/10
        </h2>
        <p>{result.text}</p>
      </section>
      <button className="big" onClick={onNext}>
        Посмотреть персональное решение →
      </button>
    </>
  )
}

function Diagnosis({ result: { diagnosis }, onNext }: NextProps & { result: DiagnosticResult }) {
  return (
    <>
      <section className="card">
        <h1>{diagnosis.title}</h1>
        {diagnosis.paragraphs.map((paragraph) => (
          <p key={paragraph}>{paragraph}</p>
        ))}
      </section>
      <section className="card">
        <h2>Что рекомендуем</h2>
        <p>{diagnosis.recommendation}</p>
      </section>
      <button className="big" onClick={onNext}>
        Продолжить →
      </button>
    </>
  )
}

function NextStep({ onNext }: NextProps) {
  return (
    <>
      <section className="card">
        <p className="label">AI DIAGNOSTICA · Ваш следующий шаг</p>
        <h1>Мы нашли, где вы теряете заявки. А что дальше?</h1>
        <p>
          Диагностика показала слабое звено вашей системы продаж. Но исправлять его наугад — значит снова тратить время
          на действия, которые могут не принести результата.
        </p>
        <p>
          Важно разобраться, почему возникла эта утечка, что уже работает в вашей системе и какие изменения дадут
          наибольший эффект именно в вашей ситуации.
        </p>
      </section>
      <section className="card">
        <h2>Следующий шаг</h2>
        <p>Разобрать вашу ситуацию глубже и определить, с чего начать изменения, чтобы не распыляться на всё сразу.</p>
      </section>
      <button className="big" onClick={onNext}>
        Узнать, как закрыть мою утечку →
      </button>
    </>
  )
}

function Invite({ onNext }: NextProps) {
  return (
    <>
      <section className="card">
        <p className="label">Персональный разбор</p>
        <h1>Давайте посмотрим, как исправить это именно в вашей системе</h1>
        <p>AI DIAGNOSTICA уже определила вашу главную утечку. Теперь я предлагаю пойти глубже.</p>
        <p>
          Я лично посмотрю результаты вашей диагностики, оценю взаимосвязь продукта, оффера, трафика и Telegram и помогу
          определить, какие изменения стоит сделать в первую очередь.
        </p>
        <p>Вам не придётся заново рассказывать обо всём с нуля — ваши ответы уже будут у меня.</p>
      </section>
      <section className="card">
        <h2>Что вы получите</h2>
        <ul>
          {BENEFITS.map((benefit) => (
            <li key={benefit}>{benefit}</li>
          ))}
        </ul>
      </section>
      <button className="big" onClick={onNext}>
        Получить персональный разбор →
      </button>
      <p className="muted note">Далее — несколько уточняющих вопросов и контакт для связи.</p>
    </>
  )
}
