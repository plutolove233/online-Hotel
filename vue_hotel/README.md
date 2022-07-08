# big_data

> A Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
# npm run mock
```


### 设置eslint规范
### 开发板块

- mock mock数据配置
- package-lock.json package的锁文件，帮我们确定安装的第三方模块的具体版本，保持团队编程的统一 

- index.html 项目默认首页模板文件 


- postcssrc.js 是对postcss的一个配置项 

- eslintrc.js 规定代码规范，不规范的进行错误提示 

- eslintignore 这里写的“build，config，dist和根目录下的JS”，eslintrc就不会对这几个家伙进行代码检测 

- editorconfig 对编辑器进行配置，比如：按空格缩两格，charset=utf-8

- .babelrc 语法解析器，对.vue文件进行转换，转换成浏览器可以识别的代码 

- static文件夹 放静态资源，比如图片，json文件 node-modules 第三方依赖的包 

- src/main.js 整个项目入口文件 

- src/app.vue 项目最原始的根组件 

- src 整个项目源代码 
  - asets 静态图片
  - directive 主要存放自定义指令 
    - permission v-haspermission(自定义是否拥有权限指令)
  - request axios请求封装
    - request 
  - layout 页面布局文件
  - publicComponents 功用组件
      - pagination 通用分页组件
  - router 路由 分模块
  - store vuex 分模块
  - style less样式
      - elememtui.less 重置elememtui样式
      - reset 重置默认样式
      - style.less 基本样式
  - utils 通用方法
      - permission.js 全局路由守卫
      - water mark.js 水印文件
  - views 页面 主要是顶部大的tab
      - login 登录页面
      - specialDisease 专病驾驶舱
      - users 用户管理
      - dataWarehouse 数据仓库
      - diseaseProject 专病项目
      - statisticalAnalysis 统计分析
      - messageCenter 消息中心






##  组件里面写方法时一定要有注释