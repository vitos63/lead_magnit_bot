type Option<T> = { value: T; label: string }

type Props<T> = {
  options: Option<T>[]
  value: T | undefined
  onChange: (value: T) => void
}

export default function Toggle<T>({ options, value, onChange }: Props<T>) {
  return (
    <div className="toggle">
      {options.map((option) => (
        <button
          key={option.label}
          className={value === option.value ? 'big' : 'big secondary'}
          aria-pressed={value === option.value}
          onClick={() => onChange(option.value)}
        >
          {option.label}
        </button>
      ))}
    </div>
  )
}
