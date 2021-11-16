import { createApp } from 'vue'

import App from './App.vue'
import './registerServiceWorker'
import router from './routes'
import store from './store'

import './assets/styles/typography.css'
import './assets/styles/tailwind.css'

createApp(App)
  .use(store)
  .use(router)
  .mount('#app')
