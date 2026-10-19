declare global {
  interface Window {
    Telegram?: {
      WebApp: {
        initData: string
        initDataUnsafe: { user?: { id: number; username?: string } }
        openLink: (url: string) => void
        openTelegramLink: (url: string) => void
        close: () => void
        expand: () => void
        disableVerticalSwipes: () => void
      }
    }
  }
}

const webApp = window.Telegram?.WebApp
const user = webApp?.initDataUnsafe.user

webApp?.expand()
webApp?.disableVerticalSwipes()

export const tgId = user?.id
export const tgUsername = user?.username
export const initData = webApp?.initData ?? ''
export const openLink = (url: string) => webApp?.openLink(url)
export const openTelegramLink = (url: string) => webApp?.openTelegramLink(url)
export const closeApp = () => webApp?.close()
