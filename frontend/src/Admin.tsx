import { useEffect, useState } from 'react'
import { type AdminPayment, type AdminUser, type AdminUserCard, getAdminUser, getAdminUsers } from './api'
import { PRODUCTS, rub } from './products'
import { type Answer, BOOL_LABELS, PRE_QUESTIONS, type Question, QUESTIONS } from './questions'
import { openTelegramLink } from './telegram'

type Filter = { label: string; match: (user: AdminUser) => boolean }

const succeeded = (payments: AdminPayment[]) => payments.filter((payment) => payment.status === 'succeeded')

const FILTERS: Filter[] = [
  { label: 'Проходят диагностику', match: (user) => user.stage === 'START' },
  { label: 'Получили результат', match: (user) => user.stage === 'GET_RESULT' && !user.skipped_review },
  { label: 'Пропустили разбор', match: (user) => user.stage === 'GET_RESULT' && user.skipped_review },
  { label: 'Заполняют преданкету', match: (user) => user.stage === 'OPEN_PRE_QUESTIONNAIRE' },
  { label: 'Отправили заявку на разбор', match: (user) => user.stage === 'SEND_PRE_QUESTIONNAIRE' },
  { label: 'Купили', match: (user) => user.stage === 'BUY_PRODUCT' },
  { label: 'Не завершили оплату', match: (user) => user.payments.length > 0 && !succeeded(user.payments).length },
]

const PAYMENT_STATUSES: Record<string, string> = {
  succeeded: 'оплачен',
  pending: 'ожидает оплаты',
  canceled: 'отменён',
}

const formatDate = (date: string) => new Date(date).toLocaleDateString('ru-RU')
const userName = (user: AdminUser) => (user.username ? `@${user.username}` : 'без username')

function stepLabel(user: AdminUser) {
  switch (user.stage) {
    case 'START':
      return `Диагностика ${user.first_answers_count}/${QUESTIONS.length}`
    case 'GET_RESULT':
      return user.skipped_review ? 'Пропустил разбор' : 'Получил результат'
    case 'OPEN_PRE_QUESTIONNAIRE':
      return `Преданкета ${user.pre_answers_count}/${PRE_QUESTIONS.length}`
    case 'SEND_PRE_QUESTIONNAIRE':
      return 'Заявка на разбор'
    default:
      return `Купил: ${succeeded(user.payments).map((payment) => PRODUCTS[payment.product].title).join(', ')}`
  }
}

export default function Admin() {
  const [users, setUsers] = useState<AdminUser[]>()
  const [error, setError] = useState('')
  const [filter, setFilter] = useState<Filter>()
  const [selected, setSelected] = useState<AdminUser>()

  useEffect(() => {
    getAdminUsers()
      .then(setUsers)
      .catch((e) => setError(e.message))
  }, [])

  if (selected) return <UserCard user={selected} onBack={() => setSelected(undefined)} />
  if (error) return <p className="error">Не загрузилось: {error}</p>
  if (!users) return <p>Загрузка…</p>

  const revenue = succeeded(users.flatMap((user) => user.payments)).reduce((sum, payment) => sum + payment.amount, 0)
  const shown = filter ? users.filter(filter.match) : users

  return (
    <main>
      <h1>Админ-панель</h1>
      <p className="muted">
        Всего: {users.length} · Выручка: {rub(revenue)}
      </p>
      <div className="card filters">
        {FILTERS.map((item) => (
          <button
            key={item.label}
            className={item === filter ? 'selected' : ''}
            onClick={() => setFilter(item === filter ? undefined : item)}
          >
            <span>{item.label}</span>
            <span>{users.filter(item.match).length}</span>
          </button>
        ))}
      </div>
      <h2>
        {filter?.label ?? 'Все пользователи'} · {shown.length}
      </h2>
      {shown.map((user) => (
        <button key={user.tg_id} className="card user" onClick={() => setSelected(user)}>
          <span>{userName(user)}</span>
          <span className="muted">
            {stepLabel(user)} · {formatDate(user.start_date)}
          </span>
        </button>
      ))}
    </main>
  )
}

function UserCard({ user, onBack }: { user: AdminUser; onBack: () => void }) {
  const [card, setCard] = useState<AdminUserCard>()
  const [error, setError] = useState('')

  useEffect(() => {
    window.scrollTo(0, 0)
    getAdminUser(user.tg_id)
      .then(setCard)
      .catch((e) => setError(e.message))
  }, [user.tg_id])

  return (
    <main>
      <button className="back" onClick={onBack}>
        ← Назад
      </button>
      <h1>{userName(user)}</h1>
      <p className="muted">
        {stepLabel(user)} · с {formatDate(user.start_date)} · tg_id {user.tg_id}
        {card?.contact && ` · контакт: ${card.contact}`}
      </p>
      {user.username && (
        <button className="big" onClick={() => openTelegramLink(`https://t.me/${user.username}`)}>
          Написать в Telegram
        </button>
      )}
      {error && <p className="error">Не загрузилось: {error}</p>}
      {card && (
        <>
          <section className="card">
            <h2>Диагностика</h2>
            {card.scores && <p className="label">{card.scores}</p>}
            <Answers questions={QUESTIONS} answers={card.first_answers} />
          </section>
          <section className="card">
            <h2>Преданкета</h2>
            <Answers questions={PRE_QUESTIONS} answers={card.pre_answers} />
          </section>
        </>
      )}
      {user.payments.length > 0 && (
        <section className="card">
          <h2>Платежи</h2>
          {user.payments.map((payment, i) => (
            <p key={i}>
              {PRODUCTS[payment.product].title} · {rub(payment.amount)} ·{' '}
              {PAYMENT_STATUSES[payment.status] ?? payment.status} · {formatDate(payment.created_at)}
            </p>
          ))}
        </section>
      )}
    </main>
  )
}

function Answers({ questions, answers }: { questions: Question[]; answers: Record<string, Answer> }) {
  const answered = questions.filter((question) => question.name in answers)
  if (!answered.length) return <p className="muted">Нет ответов</p>
  return answered.map(({ name, text, labels = BOOL_LABELS }) => {
    const answer = answers[name]
    return (
      <div key={name}>
        <p className="muted">{text}</p>
        <p className="answer">{typeof answer === 'boolean' ? labels[answer ? 0 : 1] : answer}</p>
      </div>
    )
  })
}
