import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import '../public/reset.css'



// import 'element-ui/lib/theme-chalk/index.css'

import ElementUI from 'element-ui'
import './plugins/element.js'
Vue.use(ElementUI)

Vue.prototype.$axios = axios
Vue.config.productionTip = false

new Vue({
  router,

  render: h => h(App)
}).$mount('#app')
