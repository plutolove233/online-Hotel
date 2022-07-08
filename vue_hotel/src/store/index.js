import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);
const store = new Vuex.Store({
  state:{
    userType:sessionStorage.getItem('usertype') ? JSON.parse(sessionStorage.getItem('usertype')) : null,
    token:sessionStorage.getItem('token') ? JSON.parse(sessionStorage.getItem('token')) : null,
  },
  actions:{

  },
  mutations:{
    ChangeUserType(state, payload) {
      console.log(payload)
      state.userType = payload
      sessionStorage.setItem('usertype',JSON.stringify(payload))
    },
    setToken(state,payload) {
      state.token = payload.token
      sessionStorage.setItem('token',JSON.stringify(payload.token))
    }
  },
  getters:{

  },
  modules: {},
});
export default store;
