import axios from 'axios';
import Vue from 'vue';
import qs from 'qs'

// axios.defaults.timeout = 180000; // 超时时间

const service = axios.create({
  baseURL: 'http://120.79.200.146:8000/api_1_0',
  headers: {
    'Content-Type': 'application/json;charset=UTF-8;application/octet-stream',
  },
});

service.interceptors.request.use(
  (config) => {
    config.headers.token = JSON.parse(sessionStorage.getItem('token'))
    return config;
  },

  (error) => {
    // 关闭loadding
    // 错误提示
    if (error.message && error.message.indexOf('timeout') !== -1) {
      // eslint-disable-next-line
      // console.log('请求超时');
    }
    return Promise.reject(error);
  }
);

service.interceptors.response.use(
  (res) => {
    // 对后端接口返回的code进行处理
    // console.log(res.data.err)
    // if(res.data.err >= 0) {
    //   return res.data
    // } else if (res.data.err < 0) {
    //   clearAllSession()
    //   router.push('/login')
    //   this.$message({message:res.data.msg,type:'error'})
    // }
    return res.data;
  },
  // res.data,
  // 对http返回的code进行处理
  (err) => {
    if (err && err.response) {
      switch (err.response.status) {
        case 400:
          err.message = '请求错误';
          break;

        case 401:
          // eslint-disable-next-line
          err.message = '未授权，请登录';
          break;
        case 403:
          // eslint-disable-next-line
          err.message = '拒绝访问';
          break;

        case 404:
          // eslint-disable-next-line
          err.message = `资源不存在或请求地址出错: ${err.response.config.url}`;
          break;

        case 408:
          // eslint-disable-next-line
          err.message = '请求超时';
          break;

        case 500:
          // eslint-disable-next-line
          err.message = '服务器内部错误';
          break;

        case 501:
          // eslint-disable-next-line
          err.message = '服务未实现';
          break;

        case 502:
          // eslint-disable-next-line
          err.message = '网关错误';
          break;

        case 503:
          // eslint-disable-next-line
          err.message = '服务不可用';
          break;

        case 504:
          // eslint-disable-next-line
          err.message = '网关超时';
          break;

        case 505:
          // eslint-disable-next-line
          err.message = 'HTTP版本不受支持';
          break;

        default:
          break;
      }

      Vue.prototype.$message({
        message: err.message,
        type: 'error',
        duration: 1500,
      });

      if ([401, 403].includes(err.response.status)) {
        setTimeout(() => {
          window.location.href = '/';
        }, 1500);
      }
    }
    if (err && !err.response) {
      Vue.prototype.$message({
        message: '服务器连接断开，请重新登录或稍后重试',
        type: 'error',
        duration: 1500,
      });
      setTimeout(() => {
        window.location.href = '/';
      }, 1500);
    }
    // 返回接口返回的错误信息
    return Promise.reject(err);
  }
);

export default service;
