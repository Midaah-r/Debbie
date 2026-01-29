/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        cream: {
          light: "#FDFBF7",
          DEFAULT: "#F5F0E6",
          dark: "#EAE3D2",
        },
        dark: {
          bg: "#1A1917",
          card: "#242320",
          border: "#33312E",
          text: "#EAE3D2",
        },
        warm: {
          text: "#4A453E",
          muted: "#7C7467",
          faint: "#9B9487",
        },
      },
    },
  },
  plugins: [],
};
