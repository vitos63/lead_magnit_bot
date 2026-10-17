import { useState } from 'react'

export default function ReviewChoice({ onPersonalReview }: { onPersonalReview: () => void }) {
  const [notice, setNotice] = useState('')

  return (
    <main>
      <h1>Спасибо, ответы сохранены!</h1>
      <div className="nav">
        <button className="next" onClick={onPersonalReview}>
          Личный разбор
        </button>
        <button onClick={() => setNotice('Скоро здесь появится следующий шаг')}>Пропуск разбора</button>
      </div>
      {notice && <p className="step">{notice}</p>}
    </main>
  )
}
