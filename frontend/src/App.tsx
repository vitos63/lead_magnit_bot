import { useEffect, useState } from 'react'
import Admin from './Admin'
import Analysis from './Analysis'
import { getStage, openPreQuestionnaire, skipReview } from './api'
import Offers from './Offers'
import PreQuestionnaire from './PreQuestionnaire'
import Questionnaire from './Questionnaire'
import { QUESTIONS } from './questions'
import ReviewChoice from './ReviewChoice'
import { tgId } from './telegram'

const SCREEN = new URLSearchParams(location.search).get('screen')

async function loadStage() {
  const stage = await getStage()
  if (stage === 'GET_RESULT' && SCREEN === 'offers') skipReview()
  if (stage !== 'GET_RESULT' || SCREEN !== 'pre_questionnaire') return stage
  openPreQuestionnaire()
  return 'OPEN_PRE_QUESTIONNAIRE'
}

export default function App() {
  const [stage, setStage] = useState<string | null>(null)
  const [showOffers, setShowOffers] = useState(SCREEN === 'offers')
  const [analyzing, setAnalyzing] = useState(false)

  useEffect(() => {
    if (tgId && SCREEN !== 'admin') loadStage().then(setStage).catch(() => setStage('START'))
  }, [])

  function handlePersonalReview() {
    openPreQuestionnaire()
    setStage('OPEN_PRE_QUESTIONNAIRE')
  }

  function handleSkip() {
    skipReview()
    setShowOffers(true)
  }

  if (!tgId) return <p>Откройте форму из Telegram-бота</p>
  if (SCREEN === 'admin') return <Admin />
  if (stage === null) return <p>Загрузка…</p>
  if (showOffers || stage === 'SEND_PRE_QUESTIONNAIRE' || stage === 'BUY_PRODUCT') return <Offers />
  if (stage === 'OPEN_PRE_QUESTIONNAIRE') return <PreQuestionnaire onSent={() => setStage('SEND_PRE_QUESTIONNAIRE')} />
  if (stage !== 'START') return <ReviewChoice onPersonalReview={handlePersonalReview} onSkip={handleSkip} />
  if (analyzing) return <Analysis onReady={setStage} />
  return <Questionnaire questions={QUESTIONS} url="/first_questions" onDone={() => setAnalyzing(true)} />
}
