declare global {
  interface Window {
    Telegram?: {
      WebApp: {
        initDataUnsafe: { user?: { id: number; username?: string } }
        openLink: (url: string) => void
      }
    }
  }
}

const webApp = window.Telegram?.WebApp
const user = webApp?.initDataUnsafe.user

export const tgId = user?.id
export const tgUsername = user?.username
export const openLink = (url: string) => webApp?.openLink(url)
