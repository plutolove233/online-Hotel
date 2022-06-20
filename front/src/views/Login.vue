<template>
    <div class="login_container">
      <div class="login_header">
        <my-header></my-header>
      </div>
      <div class="register_box">
        <div class="register_img">
          <!-- <img src="@/assets/images/register_bac.png" alt /> -->
        </div>
        <div class="login_box">
          <div id="top">欢迎登录</div>
  
          <el-form
            label-width="60px"
            :rules="rules"
            :model="ruleForm"
            ref="loginForm"
            class="login_form"
          >
            <el-form-item prop="username" label="账号">
              <el-input
                type="text"
                v-model="ruleForm.username"
                prefix-icon="el-icon-user"
                placeholder="用户名"
                autocomplete="off"
              ></el-input>
            </el-form-item>
            <el-form-item prop="password" label="密码">
              <el-input
                type="password"
                v-model="ruleForm.password"
                prefix-icon="el-icon-lock"
                placeholder="密码"
                autocomplete="off"
              ></el-input>
            </el-form-item>
            <el-form-item>
              <el-radio-group v-model="ruleForm.identity">
                <el-radio label="顾客"></el-radio>
                <el-radio label="酒店"></el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item class="btns">
              <el-button type="primary" @click="submitForm">登录</el-button>
              <span id="register_tips">
                还没有账号？
                <a class="forget-btn fr" href="javascript:void(0);" @click="handleJumpRegister()">立即注册</a>
              </span>
            </el-form-item>
          </el-form>
          <el-row type="flex" justify="space-between" class="user_center_elrow">
            <el-col :span="24">
              <div style="text-align: center; color: #B2B8BD">
                --------其他登录方式--------
              </div>
            </el-col>
          </el-row>
          <!-- <el-row class="user_center_elrow">
            <el-col :span="5" :offset="8">
              <img src="@/assets/images/WeChat.png" alt="" style="height: 30px;cursor: pointer;" @click="WxLogin()"/>
            </el-col>
            <el-col :span="5">
              <img src="@/assets/images/QQ.png" alt="" style="height: 30px" />
            </el-col>
          </el-row> -->
        </div>
      </div>
    </div>
  </template>
  <script>
  import { reactive, ref, toRefs } from "vue";
  import { ElMessage } from "element-plus";
//   import { APITeacherLogin } from "@/api/teacherInfo";
//   import { APIStudentLogin } from "@/api/studentInfo";
  import { localSet } from "@/utils";
  import { encryptedData } from "@/utils/jsencrypt";
  import MyHeader from "@/layout/Main/components/MyHeader.vue";
  import { useRouter } from "vue-router";
  import defaultSettings from "@/config/settings";
  export default {
    name: "Login",
    components: {
      MyHeader
    },
    setup() {
      const loginForm = ref(null);
      const router = useRouter();
      const state = reactive({
        ruleForm: {
          username: "",
          password: "",
          identity: "学生"
        },
        checked: true,
        rules: {
          username: [
            { required: "true", message: "账户不能为空", trigger: "blur" }
          ],
          password: [
            { required: "true", message: "密码不能为空", trigger: "blur" }
          ],
          identity: [{ required: "true", message: "请选择你的身份" }]
        }
      });
      const submitForm = async () => {
        loginForm.value.validate(valid => {
          if (valid) {
            if (state.ruleForm.identity === "学生") {
              APIStudentLogin({
                CollegeID: 3,
                Account: state.ruleForm.username || "",
                Password: encryptedData(state.ruleForm.password)
              })
                .then(res => {
                  res = res.data;
                  localSet("Token", res.Token);
                  localSet("StudentID", res.StudentID);
                  localSet("UserType", 1);
                  localSet("UserName", res.StudentName);
                  console.log(res.Token);
                  window.location.href = "/index";
                })
                .catch(err => {
                  console.log(err);
                  ElMessage.error({
                    message: err
                  });
                });
            } else {
              // 教师账号登录
              APITeacherLogin({
                Account: state.ruleForm.username || "",
                Password: encryptedData(state.ruleForm.password)
              })
                .then(res => {
                  res = res.data;
                  localSet("Token", res.Token);
                  localSet("TeacherID", res.TeacherID);
                  localSet("UserType", 2);
                  localSet("UserName", res.TeacherName);
                  console.log(res);
                  window.location.href = "/index";
                })
                .catch(err => {
                  console.log(err);
                  ElMessage.error({
                    message: err
                  });
                });
            }
          } else {
            console.log("error submit!!");
            return false;
          }
        });
      };
      const handleJumpRegister = () => {
        router.push({
          name: "Register"
        })
      }
      const resetForm = () => {
        loginForm.value.resetFields();
      };
      const WxLogin = async () => {
        const WxHttp = defaultSettings.WxHttp;
        const WxAppID = defaultSettings.WxAppID;
        const redirectUri = defaultSettings.redirect_uri;
        const urlcode = encodeURIComponent(redirectUri);
        const constParamas =
          "response_type=code&scope=snsapi_login&state=STATE#wechat_redirect";
        state.contents =
          WxHttp + "appid=" + WxAppID + "&redirect_uri=" + urlcode + "&" + constParamas;
        window.location.href = state.contents;
      }
      return {
        ...toRefs(state),
        loginForm,
        submitForm,
        resetForm,
        handleJumpRegister,
        WxLogin
      };
    }
  };
  </script>
  
  <style scoped>
  .login_container .register_box {
    overflow: hidden;
    margin: 0 auto;
    width: 1200px;
    position: relative;
    background-color: #fff;
  }
  #top {
    width: 100%;
    margin-bottom: 50px;
    color: rgb(102, 126, 181);
    text-align: center;
    font-size: 30px;
  }
  .register_box .login_box {
    float: right;
    width: 30%;
    margin-right: 5%;
    margin-top: 8%;
  }
  .login_container .register_img {
    float: left;
    width: 65%;
  }
  #register_tips {
    color: rgb(21, 45, 102);
    margin-left: 20px;
  }
  #register_tips a {
    text-decoration: none;
  }
  .login_container .login_header {
    background-color: #fff;
    margin-bottom: 10px;
  }
  .WeChat img {
    width: 40px;
  }
  </style>
  