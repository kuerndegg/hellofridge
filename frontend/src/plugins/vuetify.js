/**
 * plugins/vuetify.js
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
export default createVuetify({
  theme: {
    themes: {
      light: {
        colors: {
          green: '#057A46',
          light_green: '#E3FCBB',
          lime: '#98DA14',
          grey: '#6C6C6C',
          white: '#FFFFFF',
        },
      },
    },
  },
})
