import { useState } from 'react'

export default function ReviewChoice() {
  const [notice, setNotice] = useState('')
  const showNotice = () => setNotice('Скоро здесь появится следующий шаг')

  return (
    <main>
      <h1>Спасибо, ответы сохранены!</h1>
      <div className="nav">
        <button className="next" onClick={showNotice}>
          Личный разбор
        </button>
        <button onClick={showNotice}>Пропуск разбора</button>
      </div>
      {notice && <p className="step">{notice}</p>}
    </main>
  )
}
