import Vue from 'vue';
import Router from 'vue-router';
import Layout from '@/layout/index.vue';

Vue.use(Router);

const routes = [
  {
    path: '/',
    redirect: '/login',
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/login/index.vue'),
  },
  {
    path: '/index',
    name: 'index',
    component: () => import('@/views/index/index.vue'),
  },
  {
    path: '/userIndex',
    name: 'userIndex',
    component: () => import('@/views/userIndex/index.vue'),
  },
  {
    path: '/order',
    name: 'order',
    component: () => import('@/views/userIndex/order.vue'),
  },
  {
    path: '/hotelDetail',
    name: 'hotelDetail',
    component: () => import('@/views/userIndex/hotelDetail.vue'),
  },
  {
    path: '/orderMore',
    name: 'orderMore',
    component: () => import('@/views/userIndex/orderMore.vue'),
  },
  {
    path: '/paySuccess',
    name: 'paySuccess',
    component: () => import('@/views/userIndex/paySuccess.vue'),
  },
  {
    path: '/comment',
    name: 'comment',
    component: () => import('@/views/userIndex/comment.vue'),
  },
  {
    path: '/roomDetail',
    name: 'roomDetail',
    component: () => import('@/views/index/roomDetail.vue'),
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('@/views/register.vue'),
  }
];

const createRouter = () =>
  new Router({
    // 回到顶部
    scrollBehavior: () => ({ y: 0 }),
    routes,
  });

// 解决跳转相同路由报错问题
const originalPush = Router.prototype.push;
Router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch((err) => err);
};
const router = createRouter();

export function resetRouter() {
  const newRouter = createRouter();
  router.matcher = newRouter.matcher; // reset router
}

export default router;
