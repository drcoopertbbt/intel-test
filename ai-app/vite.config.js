import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Added a comment here to indicate code change for enabling new data integration.
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 5173,
  },
})
