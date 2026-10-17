type Option<T> = { value: T; label: string }

type Props<T> = {
  name: string
  options: Option<T>[]
  value: T | undefined
  onChange: (value: T) => void
}

export default function Toggle<T>({ name, options, value, onChange }: Props<T>) {
  return (
    <div className="toggle">
      {options.map((option) => (
        <label key={option.label} className={value === option.value ? 'selected' : ''}>
          <input type="radio" name={name} checked={value === option.value} onChange={() => onChange(option.value)} />
          {option.label}
        </label>
      ))}
    </div>
  )
}
