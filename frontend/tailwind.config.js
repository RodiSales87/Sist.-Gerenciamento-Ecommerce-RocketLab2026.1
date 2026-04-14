/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: '#000000',
        foreground: '#FFFFFF',
        primary: '#DDAA33',
        // Optional dark variants
        card: '#111111',
        muted: '#333333',
      }
    },
  },
  plugins: [],
}