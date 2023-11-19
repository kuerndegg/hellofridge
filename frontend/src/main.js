/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from './App.vue'

// Composables
import { createApp, watch } from 'vue'
import { createPinia } from 'pinia'

const pinia = createPinia()

watch(
    pinia.state,
    (state) => {
      sessionStorage.setItem('selectedIngredients', JSON.stringify(state.selectedIngredients));
    },
    { deep: true }
    );
  

const app = createApp(App).use(pinia)

registerPlugins(app)

app.mount('#app')
