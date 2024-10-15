/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: false,

  content: ["./**/templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["light"],
  },
};
