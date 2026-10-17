type Props = {
  onPersonalReview: () => void
  onSkip: () => void
}

export default function ReviewChoice({ onPersonalReview, onSkip }: Props) {
  return (
    <main>
      <h1>Спасибо, ответы сохранены!</h1>
      <div className="nav">
        <button className="next" onClick={onPersonalReview}>
          Личный разбор
        </button>
        <button onClick={onSkip}>Пропуск разбора</button>
      </div>
    </main>
  )
}
