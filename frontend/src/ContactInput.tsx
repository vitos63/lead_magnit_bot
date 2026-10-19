import type { Answer } from './questions'
import { tgUsername } from './telegram'
import Toggle from './Toggle'

const TELEGRAM_CONTACT = `@${tgUsername}`

const OPTIONS = [
  { value: 'telegram', label: 'Telegram' },
  { value: 'other', label: 'Другое' },
]

type Props = {
  value: Answer | undefined
  onChange: (value: Answer) => void
}

export default function ContactInput({ value, onChange }: Props) {
  const choice = value === undefined ? undefined : value === TELEGRAM_CONTACT ? 'telegram' : 'other'
  const input = (
    <input
      type="text"
      placeholder="Укажите ваш Telegram username или другой удобный способ связи"
      value={String(value ?? '')}
      onChange={(e) => onChange(e.target.value)}
    />
  )

  if (!tgUsername) return input

  return (
    <>
      <Toggle
        options={OPTIONS}
        value={choice}
        onChange={(option) => onChange(option === 'telegram' ? TELEGRAM_CONTACT : '')}
      />
      {choice === 'other' && input}
    </>
  )
}
