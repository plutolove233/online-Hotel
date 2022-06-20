<!--网页头部组件-->
<template>
  <header>
    <div id="header">
      <!-- <router-link to="/index"><img class="icon_img" src="@/assets/images/logo_01.png"/></router-link> -->
      <div id="input_register">
        <div v-if="state.is_login == false" class="login_button">
          <el-button type="text" @click="handleLogin()">登录</el-button>
          <el-button type="primary" @click="handleRegister()">注册</el-button>
        </div>
        <ul v-else-if="state.is_login == true" class="user_contain layui-nav">
          <li class="layui-nav-item">
            <a class="my_class">
              <!-- <i class="el-icon-user-solid"></i> -->
              <i>
                <svg
                  t="1625815054702"
                  class="icon"
                  viewBox="0 0 1024 1024"
                  version="1.1"
                  xmlns="http://www.w3.org/2000/svg"
                  p-id="2416"
                  width="20"
                  height="20"
                >
                  <path
                    d="M516.266667 8.533333a249.617067 249.617067 0 0 1 45.6704 495.035734C802.065067 526.472533 989.866667 728.746667 989.866667 974.9504a25.6 25.6 0 1 1-51.2 0c0-233.301333-189.098667-422.4-422.4-422.4S93.866667 741.614933 93.866667 974.9504a25.6 25.6 0 1 1-51.2 0c0-246.1696 187.8016-448.477867 427.9296-471.4496A249.617067 249.617067 0 0 1 516.266667 8.533333z m0 51.2a198.417067 198.417067 0 1 0 0 396.8 198.417067 198.417067 0 0 0 0-396.8z"
                    fill="#4E505B"
                    p-id="2417"
                  ></path>
                </svg>
              </i>
              <span style="margin-left: 5px">
                {{ state.UserName }}
              </span>
            </a>
            <dl class="layui-nav-child layui-anim-upbit">
              <dd><span @click="handlePersonalCenter()">个人中心</span></dd>
              <dd><span @click="handleOut()">退出</span></dd>
            </dl>
          </li>
        </ul>
        <div id="input_search">
          <el-input
            id="newCode"
            v-model="state.searchText"
            suffix-icon="el-icon-search"
            maxlength="60"
            placeholder="搜索    实验/老师"
          ></el-input>
        </div>
      </div>
      <div id="header_nav">
        <el-menu
          :default-active="state.activeIndex"
          class="el-menu-demo"
          mode="horizontal"
          router
        >
          <el-menu-item index="/index">首页</el-menu-item>
          <el-menu-item index="/projectlist">实验项目</el-menu-item>
          <el-menu-item index="/about">关于我们</el-menu-item>
        </el-menu>
      </div>
    </div>
  </header>
</template>

<script>
import { useRouter } from "vue-router";
import { onMounted, reactive } from "vue";
import { localGet } from "@/utils";
export default {
  data() {
    return {};
  },
  setup() {
    const router = useRouter();
    const state = reactive({
      activeIndex: "/index",
      is_login: false,
      searchText: "",
      HeadPic: "",
      ProjectCount: "",
      StudentName: "",
      TeacherName: "",
      Token: "",
      StudentID: 0,
      UserName: ""
    });
    const getUserData = () => {
      state.Token = localStorage.getItem("Token");
      state.StudentID = localStorage.getItem("StudentID");
      state.UserName = localGet("UserName");
    };
    const TestStudentToken = () => {
      if (state.Token) {
        state.is_login = true;
      }
    };
    const TestTeacherToken = () => {
      if (state.Token) {
        state.is_login = true;
      }
    };
    const handleAddress = () => {
      state.activeIndex = router.currentRoute.value.path;
    };
    const handleJump = address => {
      alert(address);
      router.push({
        path: address
      });
    };
    const handleLogin = () => {
      router.push({
        path: "/login"
      });
    };
    const handlePersonalCenter = () => {
      if (localStorage.getItem("UserType") === "1") {
        router.push({
          path: "/student"
        });
      }
      if (localStorage.getItem("UserType") === "2") {
        router.push({
          path: "/teacher"
        });
      }
    };
    const handleRegister = () => {
      router.push({
        path: "/register"
      });
    };
    const handleOut = () => {
      state.is_login = false;
      localStorage.removeItem("Token");
      localStorage.removeItem("StudentID");
      localStorage.removeItem("TeacherID");
      localStorage.removeItem("UserType");
      localStorage.removeItem("UserName");
      router.push({
        name: "index"
      });
    };
    onMounted(() => {
      handleAddress();
      getUserData();
      if (localStorage.getItem("UserType") === "1") {
        TestStudentToken();
      } else if (localStorage.getItem("UserType") === "2") {
        TestTeacherToken();
      }
    });
    // watch(() => {
    //   handleAddress();
    // })
    return {
      state,
      handleLogin,
      handleRegister,
      handleJump,
      handlePersonalCenter,
      handleAddress,
      handleOut
    };
  },
  methods: {}
};
</script>

<style scoped>
#header {
  background-color: #fff;
  margin: 0 auto;
  width: 80%;
  height: 60px;
  line-height: 60px;
  position: relative;
  margin-bottom: 10px;
}

.icon_img {
  height: 100%;
}

#input_register {
  float: right;
}

#input_search {
  float: right;
  width: 300px;
  margin: 0 5px;
}

#newCode {
  border-radius: 30px;
  border: darkgray 1px solid;
  /* background: url(@/assets/images/search.svg); */
}
.layui-nav-child {
  display: none;
  position: absolute;
  left: 0;
  top: 15px;
  min-width: 100%;
  line-height: 30px;
  padding: 5px 0;
  box-shadow: 0 2px 4px rgb(0 0 0 / 12%);
  border: 1px solid #d2d2d2;
  background-color: #fff;
  z-index: 100;
  border-radius: 2px;
  white-space: nowrap;
  -webkit-animation-duration: 0.3s;
  animation-duration: 0.3s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}
.layui-nav-child dd {
  padding-left: 10px;
  padding-right: 10px;
}
.layui-nav-child dd span {
  font-size: 14px;
}
.layui-anim-upbit :first-child:hover {
  background-color: #efefef;
}
.layui-anim-upbit :last-child:hover {
  background-color: #efefef;
}
.layui-nave {
  right: 0;
  top: 0;
  padding: 0;
}
dd {
  margin-inline-start: 0;
  cursor: pointer;
}
.layui-nav-item {
  position: relative;
  display: inline-block;
  vertical-align: middle;
  line-height: 30px;
}
.login_button {
  margin: 0 0 0 10px;
  float: right;
}

.user_contain {
  margin: 0 0 0 10px;
  float: right;
  width: 80px;
}
.user_contain .portrait_img {
  width: 100%;
  border-radius: 40px;
  margin: 0 0 0 10px;
  float: right;
}

#header_nav {
  width: 35%;
  position: absolute;
  top: 0px;
  left: 18%;
}
#header li {
  list-style: none;
}
.ative {
  display: inline-block;
  width: 20%;
  margin: 0 auto;
  text-align: center;
  line-height: 40px;
  text-decoration: none;
  color: black;
}
.personal_block {
  display: none;
  position: absolute;
  width: 150px;
  z-index: 2;
}

.user_contain:hover .layui-nav-child {
  display: block;
}
.layui-nav-item:hover .layui-nav-child {
  display: block;
}
.layui-nav-child:hover .layui-nav-child {
  display: block;
}
</style>
