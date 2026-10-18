import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/admin': 'http://127.0.0.1:8000',
      '/first_questions': 'http://127.0.0.1:8000',
      '/payments': 'http://127.0.0.1:8000',
      '/pre_questionnaire': 'http://127.0.0.1:8000',
      '/users': 'http://127.0.0.1:8000',
    },
  },
})
