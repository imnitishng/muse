var rankColors = require('./src/utils/generateColors').rankColorsMap
var rankColorsMap = {}

rankColors.forEach((colorHex, i) => {
  const colorName = `${210-(i+1)*10}`
  rankColorsMap[colorName] = colorHex
})

module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      width: {
        '1.5/12': '12.33%'
      },
      colors: {
        rankColor: rankColorsMap
      },
      fontFamily: {
        condensed: ['Saira Extra Condensed'],
        body: ['Montserrat']
      },
      boxShadow: {
        '2xl-darker': '0 25px 50px -12px rgba(0, 0, 0, 0.7)',
      },
      animation: {
        bounce200: 'bounce 1s infinite 200ms',
        bounce400: 'bounce 1s infinite 400ms',
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
