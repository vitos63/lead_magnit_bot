declare global {
  interface Window {
    Telegram?: { WebApp: { initDataUnsafe: { user?: { id: number; username?: string } } } }
  }
}

const user = window.Telegram?.WebApp.initDataUnsafe.user

export const tgId = user?.id
export const tgUsername = user?.username
