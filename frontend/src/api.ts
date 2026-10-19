import type { ProductId } from './products'
import type { Answer } from './questions'
import { initData, tgId } from './telegram'

export const POLL_INTERVAL = 3000

export type ProductPrice ={ title: string; price: number; old_price: number }

export type AdminPayment = { product: ProductId; amount: number; status: string; created_at: string }

export type AdminUser = {
  tg_id: number
  username: string | null
  start_date: string
  stage: string
  skipped_review: boolean
  first_answers_count: number
  pre_answers_count: number
  payments: AdminPayment[]
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

export async function getResult(): Promise<string> {
  const response = await request(`/first_questions/${tgId}/result`)
  return (await response.json()).text
}

export async function openPreQuestionnaire() {
  await request(`/pre_questionnaire/${tgId}/open`, {})
}

export async function skipReview() {
  await request(`/users/${tgId}/skip_review`, {})
}

export async function sendPreQuestionnaire() {
  await request(`/pre_questionnaire/${tgId}/send`, {})
}

export async function getProducts(): Promise<Record<ProductId, ProductPrice>> {
  const response = await request('/payments/products')
  return response.json()
}

export async function createPayment(product: ProductId): Promise<{ id: string; url: string }> {
  const response = await request('/payments', { tg_id: tgId, product })
  return response.json()
}

export async function getPaymentStatus(id: string): Promise<string> {
  const response = await request(`/payments/${id}`)
  return (await response.json()).status
}

export async function getAdminUsers(): Promise<AdminUser[]> {
  const response = await request('/admin/users')
  return response.json()
}

export async function getAdminUser(id: number): Promise<AdminUserCard> {
  const response = await request(`/admin/users/${id}`)
  return response.json()
}
