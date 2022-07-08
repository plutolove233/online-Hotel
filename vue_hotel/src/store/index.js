import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    path:[]
  },
  getters:{
    getToken:state =>{
      return sessionStorage.getItem('token');
    },
    getAdminInfo:state =>{//获取管理员信息
      return JSON.parse(sessionStorage.getItem('admin'))
    },
    Exit:state =>{//退出清空用户信息缓存
      sessionStorage.clear()
    },
    getPath:state =>{//获取路径信息
      return state.path
    }
   
  },
  mutations: {
    setToken:(state,tokenInfo) =>{//保存token信息到本地
      sessionStorage.setItem('token',tokenInfo)
    },
    setAdminInfo:(state,admin) => {//存储管理员信息
      sessionStorage.setItem('admin',JSON.stringify(admin));
    },
    setPath:(state,path) =>{//设置路径信息
      state.path=path
    },
    Exit:state =>{//退出清空用户信息缓存
      sessionStorage.clear()
    }
  },
  actions: {
    setToken:(context,tokenInfo) =>{//异步保存token信息到本地
      context.commit('setToken',tokenInfo)
    },
    setAdminInfo:(context,admin) =>{//保存管理员信息
      context.commit('setAdminInfo',admin)
    },
    setPath:(context,path) =>{//设置路径信息
      context.commit('setPath',path)
    },
    Exit:context =>{//用户退出
      context.commit('Exit')
    }
  },
  modules: {
  }
})
