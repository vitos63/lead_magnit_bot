declare global {
  interface Window {
    Telegram?: { WebApp: { initDataUnsafe: { user?: { id: number } } } }
  }
}

export const tgId = window.Telegram?.WebApp.initDataUnsafe.user?.id
