/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["site/templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [require('@tailwindcss/typography')]
}
