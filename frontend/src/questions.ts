export type Answer = boolean | string

export type Question = {
  name: string
  text: string
  type: 'bool' | 'text' | 'contact'
  labels?: [string, string]
  placeholder?: string
  category?: string
}

export const BOOL_LABELS: [string, string] = ['Да', 'Нет']

export const PRE_QUESTIONS: Question[] = [
  {
    name: 'what_result_you_want_to_get',
    text: 'Какой результат вы хотите получить в ближайшие 2–3 месяца?',
    type: 'text',
    placeholder: 'Например: увеличить количество заявок, выйти на новый уровень дохода…',
  },
  {
    name: 'what_mostly_hinder',
    text: 'Что сейчас больше всего мешает вам увеличить количество заявок?',
    type: 'text',
    placeholder: 'Расскажите, что уже пробовали и с чем возникают сложности…',
  },
  {
    name: 'are_you_ready',
    text: 'Готовы ли вы внедрять изменения в ближайший месяц?',
    type: 'bool',
    labels: ['Да, готов(а) действовать', 'Пока изучаю варианты'],
  },
  { name: 'contact', text: 'Как с вами удобнее связаться?', type: 'contact' },
]

export const QUESTIONS: Question[] = [
  {
    name: 'has_product',
    text: 'У вас есть конкретный продукт или услуга с понятным результатом, стоимостью и форматом работы?',
    type: 'bool',
    category: 'ПРОДУКТ',
  },
  {
    name: 'product_description',
    text: 'Что именно вы сейчас продаёте? Опишите продукт, для кого он и какой результат получает клиент.',
    type: 'text',
    category: 'ПРОДУКТ',
  },
  {
    name: 'ten_seconds',
    text: 'Может ли новый человек за 10 секунд понять, какую проблему решает ваш продукт и почему стоит обратиться именно к вам?',
    type: 'bool',
    category: 'ПРОДУКТ',
  },
  {
    name: 'has_offer',
    text: 'Есть ли у вас конкретное предложение, которое вы регулярно озвучиваете потенциальным клиентам?',
    type: 'bool',
    category: 'ОФФЕР',
  },
  {
    name: 'offer_description',
    text: 'Напишите ваше текущее предложение клиенту так, как вы обычно формулируете его в посте или переписке.',
    type: 'text',
    category: 'ОФФЕР',
  },
  {
    name: 'channels',
    text: 'Из каких каналов привлекаете холодную целевую аудиторию? Есть ли органические каналы привода целевой аудитории (бесплатные)?',
    type: 'text',
    category: 'ТРАФИК',
  },
  {
    name: 'main_channel',
    text: 'Есть ли у вас один основной канал, из которого вы регулярно привлекаете новую аудиторию?',
    type: 'bool',
    category: 'ТРАФИК',
  },
  { name: 'tries', text: 'Что вы уже пробовали для привлечения новых людей?', type: 'text', category: 'ТРАФИК' },
  {
    name: 'thirty',
    text: 'Понятно ли новому посетителю вашего Telegram-канала за 30 секунд, кому вы помогаете и что предлагаете?',
    type: 'bool',
    category: 'TELEGRAM',
  },
  {
    name: 'has_next_step',
    text: 'Есть ли в Telegram понятный следующий шаг: написать вам, оставить заявку, пройти диагностику или записаться на консультацию?',
    type: 'bool',
    category: 'TELEGRAM',
  },
  {
    name: 'pin_post',
    text: 'Есть ли у вас закреплённый пост или другой понятный маршрут, который знакомит нового подписчика с вами, продуктом и результатами клиентов?',
    type: 'bool',
    category: 'TELEGRAM',
  },
  {
    name: 'client_must_to_do',
    text: 'Представьте, что потенциальный клиент заинтересовался вашим контентом. Что конкретно он должен сделать дальше, чтобы стать вашим клиентом?',
    type: 'text',
    category: 'TELEGRAM',
  },
]
