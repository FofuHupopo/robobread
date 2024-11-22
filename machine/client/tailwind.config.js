/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            gridTemplateColumns: {
                // Simple 16 column grid
                'layout': '358px 722px',
            },
            colors: {
                layoutColor: '#F8F8F8',
                layoutLine: '#E3E3E3',
                selectCategory: '#F1F1F1',
                helpBgHome: 'rgba(248, 248, 248, .32)',
                helpBg: '#F8F8F8',
                orange: '#FFA30E',
                cardProductComposition: '#F5F5F5',
                buttonBg: '#D9D9D9',
                textGrey: '#434343',
                textGreySecond: '#B8B8B8',
                contactColor: "#434343"

            },
            backgroundImage: {
                'home': "url('/src/assets/home.png')",
            }
        },
    },
    plugins: [],
}

