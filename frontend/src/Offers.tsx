import { useEffect, useState } from 'react'
import { getProducts, type ProductPrice } from './api'
import ProductScreen from './ProductScreen'
import { PRODUCTS, type ProductId } from './products'

export default function Offers() {
  const [prices, setPrices] = useState<Record<ProductId, ProductPrice>>()
  const [selected, setSelected] = useState<ProductId>()

  useEffect(() => {
    getProducts().then(setPrices)
  }, [])

  if (selected) return <ProductScreen id={selected} price={prices?.[selected]} onBack={() => setSelected(undefined)} />

  return (
    <main>
      <h1 className="product-title">Я подготовила для вас 2 решения</h1>
      <p>Теперь вы знаете, где теряете заявки. Пора это исправить.</p>
      <p className="muted">
        Выбирайте, как хотите двигаться дальше: вместе со мной, с моим личным сопровождением или самостоятельно с
        готовыми AI-инструментами.
      </p>
      {(Object.keys(PRODUCTS) as ProductId[]).map((id) => {
        const { card } = PRODUCTS[id]
        return (
          <section key={id} className="card">
            <h2>{card.title}</h2>
            <p>{card.text}</p>
            {card.bonus && <p className="muted">{card.bonus}</p>}
            <button className="big" onClick={() => setSelected(id)}>
              {card.button}
            </button>
          </section>
        )
      })}
    </main>
  )
}
