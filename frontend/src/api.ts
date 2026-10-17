import type { Answer } from './questions'
import { tgId } from './telegram'

async function request(url: string, body?: object) {
  const init = body && { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) }
  const response = await fetch(url, init)
  if (!response.ok) throw new Error(`HTTP ${response.status}`)
  return response
}

export async function saveAnswer(url: string, question: string, answer: Answer) {
  await request(url, { tg_id: tgId, question, answer })
}

export async function getStage(): Promise<string> {
  const response = await request(`/users/${tgId}`)
  return (await response.json()).stage
}

export async function openPreQuestionnaire() {
  await request(`/pre_questionnaire/${tgId}/open`, {})
}

export async function sendPreQuestionnaire() {
  await request(`/pre_questionnaire/${tgId}/send`, {})
}
