import { useState } from 'react'
import { sendPreQuestionnaire } from './api'
import { PRE_QUESTIONS } from './questions'
import Questionnaire from './Questionnaire'

export default function PreQuestionnaire({ onSent }: { onSent: () => void }) {
  const [consent, setConsent] = useState(false)

  return (
    <Questionnaire
      questions={PRE_QUESTIONS}
      url="/pre_questionnaire"
      intro={
        <section className="card">
          <p className="label">Персональный разбор · Анкета</p>
          <h1>Давайте разберём вашу ситуацию предметно</h1>
          <p>
            Я уже получила результаты вашей диагностики. Поэтому не буду просить вас заново рассказывать о продукте,
            аудитории и каналах привлечения.
          </p>
          <p>
            Ответьте ещё на несколько вопросов, чтобы я понимала, какой результат вы хотите получить и насколько сейчас
            готовы к изменениям.
          </p>
        </section>
      }
      doneLabel="Отправить заявку на разбор →"
      canFinish={consent}
      onDone={() => sendPreQuestionnaire().then(onSent)}
    >
      <label className="consent">
        <input type="checkbox" checked={consent} onChange={(e) => setConsent(e.target.checked)} />
        Я согласен(на) на обработку предоставленных данных для рассмотрения моей заявки и на связь со мной по поводу
        персонального разбора.
      </label>
    </Questionnaire>
  )
}
