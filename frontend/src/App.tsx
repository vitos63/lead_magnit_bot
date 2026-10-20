import { useEffect, useState } from 'react'
import Admin from './Admin'
import Analysis from './Analysis'
import { getStage, openPreQuestionnaire } from './api'
import PreQuestionnaire from './PreQuestionnaire'
import Questionnaire from './Questionnaire'
import { QUESTIONS } from './questions'
import RequestSent from './RequestSent'
import Result from './Result'
import { tgId } from './telegram'

const SCREEN = new URLSearchParams(location.search).get('screen')

export default function App() {
  const [stage, setStage] = useState<string | null>(null)
  const [analyzing, setAnalyzing] = useState(false)

  useEffect(() => {
    if (tgId && SCREEN !== 'admin') getStage().then(setStage).catch(() => setStage('START'))
  }, [])

  function handlePersonalReview() {
    openPreQuestionnaire()
    setStage('OPEN_PRE_QUESTIONNAIRE')
  }

  if (!tgId) return <p>Откройте форму из Telegram-бота</p>
  if (SCREEN === 'admin') return <Admin />
  if (stage === null) return <p>Загрузка…</p>
  if (stage === 'SEND_PRE_QUESTIONNAIRE') return <RequestSent />
  if (stage === 'OPEN_PRE_QUESTIONNAIRE') return <PreQuestionnaire onSent={() => setStage('SEND_PRE_QUESTIONNAIRE')} />
  if (stage !== 'START') return <Result onPersonalReview={handlePersonalReview} />
  if (analyzing) return <Analysis onReady={setStage} />
  return <Questionnaire questions={QUESTIONS} url="/first_questions" onDone={() => setAnalyzing(true)} />
}
