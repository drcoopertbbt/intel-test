import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0', // Binds the development server to all available network interfaces
    port: 5173, // Default port, change if necessary
  },
})
