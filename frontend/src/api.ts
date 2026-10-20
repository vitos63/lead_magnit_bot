import type { Answer } from './questions'
import { initData, tgId } from './telegram'

export const POLL_INTERVAL = 3000

export type Result = { directions: { title: string; score: number }[]; leak: string; text: string }

export type AdminUser = {
  tg_id: number
  username: string | null
  start_date: string
  stage: string
  first_answers_count: number
  pre_answers_count: number
}

export type AdminUserCard = AdminUser & {
  contact: string | null
  scores: string | null
  first_answers: Record<string, Answer>
  pre_answers: Record<string, Answer>
}

async function request(url: string, body?: object) {
  const response = await fetch(url, {
    headers: { 'Content-Type': 'application/json', 'X-Init-Data': initData },
    ...(body && { method: 'POST', body: JSON.stringify(body) }),
  })
  if (!response.ok) throw new Error(`HTTP ${response.status}`)
  return response
}

export async function saveAnswer(url: string, question: string, answer: Answer) {
  await request(url, { tg_id: tgId, question, answer })
}

export async function getAnswers(url: string): Promise<Record<string, Answer>> {
  const response = await request(`${url}/${tgId}`)
  return response.json()
}

export async function getStage(): Promise<string> {
  const response = await request(`/users/${tgId}`)
  return (await response.json()).stage
}

export async function getResult(): Promise<Result> {
  const response = await request(`/first_questions/${tgId}/result`)
  return response.json()
}

export async function openPreQuestionnaire() {
  await request(`/pre_questionnaire/${tgId}/open`, {})
}

export async function sendPreQuestionnaire() {
  await request(`/pre_questionnaire/${tgId}/send`, {})
}

export async function getAdminUsers(): Promise<AdminUser[]> {
  const response = await request('/admin/users')
  return response.json()
}

export async function getAdminUser(id: number): Promise<AdminUserCard> {
  const response = await request(`/admin/users/${id}`)
  return response.json()
}
