import 'bootstrap'
import "bootswatch/dist/cyborg/bootstrap.min.css";
// setting fotawesome to avoid inline style
import '@fortawesome/fontawesome-svg-core/styles.css'; // import usable styles manual
import { config } from '@fortawesome/fontawesome-svg-core';
config.autoAddCss = false; // disable auto add css for fontawesome
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
