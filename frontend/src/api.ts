import type { Answer } from './questions'
import { tgId } from './telegram'

export async function saveAnswer(question: string, answer: Answer) {
  const response = await fetch('/first_questions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ tg_id: tgId, question, answer }),
  })
  if (!response.ok) throw new Error(`HTTP ${response.status}`)
}
