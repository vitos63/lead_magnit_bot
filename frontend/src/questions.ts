export type Answer = boolean | string

type Question = {
  name: string
  text: string
  type: 'bool' | 'text'
}

export const QUESTIONS: Question[] = [
  { name: 'has_product', text: 'Есть ли у вас продукт?', type: 'bool' },
  { name: 'product_description', text: 'Опишите продукт', type: 'text' },
  { name: 'ten_seconds', text: 'Можно ли за 10 секунд понять, что вы предлагаете?', type: 'bool' },
  { name: 'has_offer', text: 'Есть ли у вас оффер?', type: 'bool' },
  { name: 'offer_description', text: 'Опишите оффер', type: 'text' },
  { name: 'channels', text: 'Какие каналы привлечения используете?', type: 'text' },
  { name: 'main_channel', text: 'Есть ли основной канал?', type: 'bool' },
  { name: 'tries', text: 'Что уже пробовали?', type: 'text' },
  { name: 'thirty', text: 'Тридцать (thirty)', type: 'bool' },
  { name: 'has_next_step', text: 'Есть ли у клиента понятный следующий шаг?', type: 'bool' },
  { name: 'pin_post', text: 'Есть ли закреплённый пост?', type: 'bool' },
  { name: 'client_must_to_do', text: 'Что клиент должен сделать?', type: 'text' },
]
