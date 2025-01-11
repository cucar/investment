import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000
  },
  build: {
    outDir: 'dist',
  },
  resolve: {
    alias: {
      // If you're using path aliases in CRA
      '@': '/src'
    }
  }
}) 