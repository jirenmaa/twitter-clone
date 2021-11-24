module.exports = {
  purge: ['./src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        current: '#cccccc',
        black: '#111111',
        dark: '#181818',
        active: '#34d399',
        body: '#131313',
        peach: '#707070',
        'dark-light': '#202020',
        'dark-grey': '#333333',
        'dark-peach': '#91887d',
      },
      fontSize: {
        mm: ['0.75rem', {
          lineHeight: '15px',
        }],
        ms: '0.9rem',
        '10xl': '10rem'
      },
      lineHeight: {
        none: '0'
      },
      width: {
        input: '32rem',
        form: '36rem',
        'reply-form': '40rem',
        '0.25': '0.075rem'
      },
      scale: {
        80: '.8'
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
