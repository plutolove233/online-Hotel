<template>
    <div class="register_container">
      <div class="register_header">
        <my-header></my-header>
      </div>
      <div id="register_main">
        <div class="register_img">
          <!-- <img src="../../assets/images/register_bac.png" alt="" /> -->
        </div>
        <div id="register_content">
          <div id="register_box">
            <el-form
              ref="registerFormRef"
              :model="registerForm"
              label-width="80px"
              :rules="registerFormRules"
            >
              <el-form-item
                label="学号"
                placeholder="请填写"
                prop="StudentNumber"
              >
                <el-input v-model="registerForm.StudentNumber"></el-input>
              </el-form-item>
              <el-form-item label="姓名" placeholder="请填写" prop="StudentName">
                <el-input v-model="registerForm.StudentName"></el-input>
              </el-form-item>
  
              <el-form-item label="手机号" prop="Mobile">
                <el-input
                  v-model="registerForm.Mobile"
                  placeholder="手机号为默认为您的登录账号"
                ></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="Password">
                <el-input
                  v-model="registerForm.Password"
                  placeholder="至少六位字符"
                ></el-input>
              </el-form-item>
              <el-form-item label="所属学院" prop="CollegeID">
                <el-select
                  v-model="registerForm.CollegeID"
                  filterable
                  placeholder="请选择"
                  @change="selectCollege"
                >
                  <el-option
                    v-for="item in CollegeList"
                    :key="item.CollegeID"
                    :label="item.CollegeName"
                    :value="item.CollegeID"
                  />
                </el-select>
              </el-form-item>
              <el-form-item label="所属班级" prop="ClassID">
                <el-select
                  v-model="registerForm.ClassID"
                  filterable
                  placeholder="请选择"
                >
                  <el-option
                    v-for="item in ClassList"
                    :key="item.ClassID"
                    :label="item.ClassName"
                    :value="item.ClassID"
                  />
                </el-select>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="registerSubmit"
                  >完成注册并登录</el-button
                >
                <div id="register_tips">
                  已有账号？<a class="forget-btn fr" href="javascript:void(0);" @click="handleJumpLogin()"
                    >登录</a
                  >
                </div>
              </el-form-item>
            </el-form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import MyHeader from "@/layout/Main/components/MyHeader.vue";
//   import { APIStudentRegister } from "@/api/studentInfo";
  import { reactive, ref, toRefs, onMounted } from "vue";
  import { ElMessage } from "element-plus";
  import { useRouter } from "vue-router";
//   import { APIFetchClassList } from "@/api/class";
//   import { APIFetchCollegeList } from "@/api/college";
  export default {
    components: { MyHeader },
    data() {
      return {
        radio: "1"
      };
    },
    setup() {
      const registerFormRef = ref(null);
      const router = useRouter();
      const state = reactive({
        ClassList: "", // 定义班级列表信息
        CollegeList: [], // 定义学院列表信息
        registerForm: {
          Account: "",
          Mobile: "",
          Password: "",
          StudentName: "",
          StudentNumber: "",
          CollegeID: 3,
          ClassID: ""
        },
        registerFormRules: {
          Account: [
            { required: "true", message: "账号不能为空", trigger: "blur" }
          ],
          Password: [
            { required: "true", message: "密码不能为空", trigger: "blur" }
          ],
          StudentName: [
            { required: "true", message: "姓名不能为空", trigger: "blur" }
          ],
          Mobile: [
            { required: "true", message: "手机号不能为空", trigger: "blur" }
          ],
          StudentNumber: [
            { required: "true", message: "学号不能为空", trigger: "blur" }
          ],
          ClassID: [
            { required: "true", message: "请选择班级", trigger: "change" }
          ]
        }
      });
  
      onMounted(() => {
        getCollegeList();
        getClassList();
      });
      // 获取班级列表
      const getClassList = () => {
        const userinfo = {
          UserID: localStorage.StudentID || "",
          UserType: localStorage.UserType,
          CollegeID: state.registerForm.CollegeID
        };
        const params = {
          ...userinfo,
          Page: 1,
          Size: 99999
        };
        APIFetchClassList(params)
          .then(res => {
            // console.log('Class List', res)
            state.ClassList = res.data;
          })
          .catch(err => {
            console.log("Class List", err);
            ElMessage.error({
              message: err
            });
          });
      };
  
      // 获取学院列表
      const getCollegeList = () => {
        // state.loading = true
        APIFetchCollegeList({
          UserID: localStorage.StudentID || "",
          UserType: localStorage.UserType,
          Page: 1,
          Size: 99999
        })
          .then(res => {
            // console.log('Class List', res)
            state.CollegeList = res.data;
          })
          .catch(err => {
            console.log("Class List", err);
            ElMessage.error({
              message: err
            });
          });
      };
      // 选择学院后，加载相应的班级
      const selectCollege = async () => {
        getClassList();
      };
  
      // 学生注册接口
      const registerSubmit = async () => {
        registerFormRef.value.validate(valid => {
          if (valid) {
            const params = {
              ...state.registerForm
            };
            APIStudentRegister(params)
              .then(res => {
                ElMessage.success("注册账号成功");
                router.push({ name: "Login" });
              })
              .catch(err => {
                console.log(err);
                ElMessage.error({
                  message: err
                });
              });
          }
        });
      };
      const handleJumpLogin = () => {
        router.push({
          name: 'Login'
        })
      }
      return {
        ...toRefs(state),
        registerFormRef,
        getCollegeList,
        getClassList,
        selectCollege,
        registerSubmit,
        handleJumpLogin
      };
    }
  };
  </script>
  
  <style scoped>
  .register_container #register_main {
    overflow: hidden;
    margin: 0 auto;
    width: 1200px;
    background-color: #fff;
  }
  .register_container #register_content {
    float: right;
    width: 30%;
    margin-right: 5%;
    margin-top: 3%;
  }
  .register_header {
    margin-bottom: 10px;
  }
  .register_container .register_img {
    float: left;
    width: 65%;
  }
  .register_container .register_header {
    background-color: #fff;
  }
  .register_container #register_tips {
    float: right;
    color: rgb(102, 126, 181);
  }
  </style>
  