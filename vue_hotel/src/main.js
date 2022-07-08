import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from './api/axios.js'//引入自己封装的axios
import 'font-awesome/css/font-awesome.css';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';




Vue.use(ElementUI);
Vue.prototype.$axios=axios

Vue.config.productionTip = false

router.beforeEach((to,from,next) =>{
  store.dispatch('setPath',to.matched)
  next()
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
