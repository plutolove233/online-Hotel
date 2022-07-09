// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

import 'element-ui/lib/theme-chalk/index.css';
import 'lib-flexible/flexible.js';
import Vue from 'vue';
import ElementUI from 'element-ui';
import App from './App';
import router from './router';
import store from '@/store/index.js';
import axios from 'axios';
Vue.config.productionTip = false;
Vue.use(ElementUI);
Vue.prototype.$axios = axios
Vue.prototype.$store = store
/* eslint-disable no-new */




new Vue({
  el: '#app',
  router,
  store,
  Vue,
  components: {
    App,
  },
  watch: {
  },
  computed: {
  },
  async created() {
  },
  methods: {
  },
  watch:{
  },
  template: '<App/>',
});
// eslint-disable-next-line
