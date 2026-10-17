import { useEffect, useState } from 'react'
import { getStage, openPreQuestionnaire } from './api'
import PreQuestionnaire from './PreQuestionnaire'
import Questionnaire from './Questionnaire'
import { QUESTIONS } from './questions'
import ReviewChoice from './ReviewChoice'
import { tgId } from './telegram'

const OPENED_FOR_PRE_QUESTIONNAIRE = new URLSearchParams(location.search).get('screen') === 'pre_questionnaire'

async function loadStage() {
  const stage = await getStage()
  if (stage !== 'GET_RESULT' || !OPENED_FOR_PRE_QUESTIONNAIRE) return stage
  openPreQuestionnaire()
  return 'OPEN_PRE_QUESTIONNAIRE'
}

export default function App() {
  const [stage, setStage] = useState<string | null>(null)

  useEffect(() => {
    if (tgId) loadStage().then(setStage).catch(() => setStage('START'))
  }, [])

  function handlePersonalReview() {
    openPreQuestionnaire()
    setStage('OPEN_PRE_QUESTIONNAIRE')
  }

  if (!tgId) return <p>Откройте форму из Telegram-бота</p>
  if (stage === null) return <p>Загрузка…</p>
  if (stage === 'SEND_PRE_QUESTIONNAIRE') return <p>Заявка на разбор отправлена!</p>
  if (stage === 'OPEN_PRE_QUESTIONNAIRE') return <PreQuestionnaire onSent={() => setStage('SEND_PRE_QUESTIONNAIRE')} />
  if (stage !== 'START') return <ReviewChoice onPersonalReview={handlePersonalReview} />
  return <Questionnaire questions={QUESTIONS} url="/first_questions" onDone={() => setStage('GET_RESULT')} />
}
