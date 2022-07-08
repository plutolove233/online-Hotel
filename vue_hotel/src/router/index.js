import Vue from 'vue'
import VueRouter from 'vue-router'

const Home = () => import('../views/Home.vue')//主页
const Login = () => import('../views/Login.vue')//登录页面
const Register = () => import('../views/Register.vue')//注册页面
const Room = () => import('../views/Room.vue')//房间管理页面
const RoomType = () => import('../views/RoomType.vue')//房间类型页面
const Order = () => import('../views/Order.vue')//订单页面
const OrderTracking = () => import('../views/OrderTracking.vue')//订单追踪管理页面
const Customer = () => import('../views/Customer.vue')//顾客信息管理页面
const NotFound = () => import('../views/NotFound.vue')//404页面
const NotToken = () => import('../views/NotToken.vue')//token失效页面
Vue.use(VueRouter)

  const routes = [
    {
      path:'/',
      redirect:'/login'
    },
    {
      path:'/login',
      name:'Login',
      meta:{
        title:'登录',
        permission:['admin','user']
      },
      component:Login
    },
    {
      path:'/register',
      name:'Register',
      meta:{
        title:'注册',
        permission:['admin','user']
      },
      component:Register
    },
    {
      path:'/home',
      name:'Home',
      meta:{
        title:'首页',
        permission:['admin','user']
      },
      component:Home,
      children:[
        {
          path:'room',
          name:'roomAdmin',
          meta:{
            title:'房间管理',
            permission:['admin','user']
          },
          component:Room
        },
        {
          path:'roomtype',
          name:'roomTypeAdmin',
          meta:{
            title:'房间类型管理',
            permission:['admin','user']
          },
          component:RoomType
        },
        {
          path:'order',
          name:'orderAdmin',
          meta:{
            title:'订单管理',
            permission:['admin','user']
          },
          component:Order
        },
        {
          path:'ordertracking',
          name:'orderTrackingAdmin',
          meta:{
            title:'订单追踪管理',
            permission:['admin','user']
          },
          component:OrderTracking
        },
        {
          path:'customer',
          name:'customerAdmin',
          meta:{
            title:'顾客信息管理',
            permission:['admin','user']
          },
          component:Customer
        },
        {
          path:'notfound',
          name:'notFound',
          meta:{
            title:'404页面'
          },
          component:NotFound
        },
        {
          path:'notoken',
          name:'notToken',
          meta:{
            title:'token失效页面'
          },
          component:NotToken
        }
      ]
    }
  ]

const router = new VueRouter({
  mode:'history',
  base: process.env.BASE_URL,
  routes
})


export default router
