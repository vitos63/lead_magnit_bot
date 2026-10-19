import { useEffect, useState } from 'react'
import { createPayment, getPaymentStatus, POLL_INTERVAL, type ProductPrice } from './api'
import { PRODUCTS, type ProductId, rub, type Section } from './products'
import { closeApp, openLink } from './telegram'

type Props = {
  id: ProductId
  price: ProductPrice | undefined
  onBack: () => void
}

export default function ProductScreen({ id, price, onBack }: Props) {
  const product = PRODUCTS[id]
  const [paying, setPaying] = useState(false)
  const [error, setError] = useState('')
  const [paymentId, setPaymentId] = useState<string>()
  const [status, setStatus] = useState('')

  useEffect(() => {
    window.scrollTo(0, 0)
  }, [])

  useEffect(() => {
    if (!paymentId) return
    const timer = setInterval(async () => {
      const current = await getPaymentStatus(paymentId).catch(() => 'pending')
      setStatus(current)
      if (current !== 'pending') clearInterval(timer)
    }, POLL_INTERVAL)
    return () => clearInterval(timer)
  }, [paymentId])

  async function handleBuy() {
    setPaying(true)
    setError('')
    try {
      const payment = await createPayment(id)
      openLink(payment.url)
      setPaymentId(payment.id)
      setStatus('pending')
    } catch (e) {
      setError((e as Error).message)
    } finally {
      setPaying(false)
    }
  }

  if (status === 'succeeded')
    return (
      <main className="centered">
        <h1>Оплата прошла!</h1>
        <p>{product.title}</p>
        <p className="muted">Доступ скоро появится в чате с ботом.</p>
        <button className="big" onClick={closeApp}>
          Вернуться в бота
        </button>
      </main>
    )

  return (
    <main>
      <button className="back" onClick={onBack}>
        ← Назад
      </button>
      {product.label && <p className="label">{product.label}</p>}
      <h1 className="product-title">{product.title}</h1>
      {product.subtitle && <p className="label">{product.subtitle}</p>}
      {product.sections.map((section, i) => (
        <SectionBlock key={i} {...section} />
      ))}
      <div className="card">
        <p className="label">Бонус при покупке сейчас</p>
        <SectionBlock {...product.bonus} />
      </div>
      {price && (
        <div className="price">
          {product.priceTitle && <p className="muted">{product.priceTitle}</p>}
          <p>
            <s>{rub(price.old_price)}</s> <strong>{rub(price.price)}</strong>
          </p>
          {product.priceNote && <p className="muted">{product.priceNote}</p>}
        </div>
      )}
      <button className="big" disabled={!price || paying} onClick={handleBuy}>
        {product.button(price ? rub(price.price) : '…')}
      </button>
      {status === 'pending' && <p className="muted">Ждём подтверждения оплаты…</p>}
      {status === 'canceled' && <p className="error">Оплата не прошла, попробуйте ещё раз</p>}
      {error && <p className="error">Не получилось открыть оплату: {error}</p>}
    </main>
  )
}

function SectionBlock({ title, text, items }: Section) {
  return (
    <section>
      {title && <h2>{title}</h2>}
      {text && <p>{text}</p>}
      {items && (
        <ul>
          {items.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      )}
    </section>
  )
}
