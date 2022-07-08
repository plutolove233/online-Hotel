import axios from 'axios'//引入axios框架
import router from '../router/index.js'//引入路由模块
import store from '../store/index'//引入vuex全局状态管理中心
import ElementUI from 'element-ui'//使用elementUI
import 'element-ui/lib/theme-chalk/index.css'//使用elementUI的css
import apiConfig from './apiConfig.js'//引入api配置信息

const instance = axios.create({
        baseURL: apiConfig.baseURL,//全局请求地址
        timeout: apiConfig.timeout//请求超时时间
    })

instance.interceptors.request.use(config => {//请求全局代理
    // Do something before request is sent
    config.headers.Token = localStorage.getItem("token")
    return config;
  }, error => {
    // Do something with request error
    return Promise.reject(error);
  });

instance.interceptors.response.use(response => {//响应全局代理
  // Do something before response is sent
    const { data } = response
    return data
  }, error => {
    if (error.response) {
      if(error.response.status == 401){
        ElementUI.Message({
          type:'error',
          message:'token错误！请退出并重新登录!',
          duration:2000
        })
        router.push('/home/notoken')
      }else if(error.response.status == 404){
        ElementUI.Message({
          type:'error',
          message:'404页面找不到',
          duration:2000
        })
        router.push('/home/notfound')
      }
    }
    return Promise.reject(error)
  });

  export default instance