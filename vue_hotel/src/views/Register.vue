<template>
  <div class="register">
    <div class="box">
      <div class="head">
        <img src="../assets/images/undraw_decorative_friends_q2np.svg" alt="" />
      </div>
      <div>
        <el-form
          :model="ruleForm"
          status-icon
          ref="ruleForm"
          label-width="80px"
          :rules="rules"
        >
          <el-form-item label="账号" prop="HotelAccount">
            <el-input
              v-model.trim="ruleForm.HotelAccount"
              autocomplete="off"
              clearable
            ></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="Password">
            <el-input
              type="password"
              v-model="ruleForm.Password"
              autocomplete="off"
              show-password
            ></el-input>
          </el-form-item>
          <el-form-item label="确认密码" prop="CheckPassword">
            <el-input
              type="password"
              v-model="ruleForm.CheckPassword"
              autocomplete="off"
              show-password
            ></el-input>
          </el-form-item>
          <el-form-item label="酒店名称" prop="HotelName">
            <el-input
              v-model.trim="ruleForm.HotelName"
              autocomplete="off"
              clearable
            ></el-input>
          </el-form-item>
          <el-form-item label="邮箱" prop="Email">
            <el-input
              v-model.trim="ruleForm.Email"
              autocomplete="off"
              clearable
            ></el-input>
          </el-form-item>
          <el-form-item label="手机号码" prop="Phone">
            <el-input
              v-model.trim="ruleForm.Phone"
              autocomplete="off"
              clearable
            ></el-input>
          </el-form-item>
          <el-form-item label="省市区" prop="Province">
            <el-cascader
              size="large"
              :options="options"
              v-model="selectedOptions"
              @change="handleChange"
            >
            </el-cascader>
          </el-form-item>
          <el-form-item label="具体地址" prop="Address">
            <el-input
              v-model.trim="ruleForm.Address"
              autocomplete="off"
              clearable
            ></el-input>
          </el-form-item>

          <el-form-item>
            <el-button type="warning" @click="register">注册</el-button>
            <el-button @click="resetForm">重置</el-button>
            <el-button type="text" @click="toLogin">登录</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>


<script>
import { regionData } from "element-china-area-data";
import { paramsToFormData } from "../utils/parasmToFormData";

export default {
  name: "Register",
  data() {
    const checkEmail = (rule, value, callback) => {
      var regEmail =
        /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
      if (regEmail.test(value)) {
        return callback();
      } else if (value === "") {
        callback(new Error("请输入邮箱"));
      } else {
        callback(new Error("邮箱格式错误！"));
      }
    };

    const checkPhone = (rule, value, callback) => {
      var regPhone = 11 && /^((13|14|15|17|18)[0-9]{1}\d{8})$/;
      if (regPhone.test(value)) {
        return callback();
      } else if (value === "") {
        callback(new Error("请输入手机号码"));
      } else {
        callback(new Error("手机号码格式错误!"));
      }
    };

    return {
      options: regionData,
      selectedOptions: [],
      ruleForm: {
        HotelAccount: "",
        Password: "",
        CheckPassword: "",
        HotelName: "",
        Email: "",
        Phone: "",
        Address: "",
        Province: "",
        City: "",
        Area: "",
      },

      rules: {
        HotelAccount: [
          { required: true, message: "请输入注册账号", trigger: "blur" },
        ],
        Password: [
          { required: true, message: "请输入注册密码", trigger: "blur" },
        ],
        CheckPassword: [
          { required: true, message: "请再次输入密码", trigger: "blur" },
        ],
        HotelName: [
          { required: true, message: "请输入酒店名称", trigger: "blur" },
        ],
        Email: [{ required: true, validator: checkEmail, trigger: "blur" }],
        Phone: [{ required: true, trigger: "blur", validator: checkPhone }],
        Address: [
          { required: true, message: "请输入具体地址", trigger: "blur" },
        ],
      },
    };
  },

  methods: {
    handleChange(value) {
      console.log(value);
    },
    toLogin: function () {
      //去登录界面
      this.$router.push("/login");
    },
    resetForm: function () {
      //重置注册信息
      this.$refs.ruleForm.resetFields();
    },
    register: function () {
      //注册
      let empty =
        this.ruleForm.HotelAccount == "" ||
        this.ruleForm.Password == "" ||
        this.ruleForm.CheckPassword == "" ||
        this.ruleForm.HotelName == "" ||
        this.ruleForm.Email == "" ||
        this.ruleForm.Address == "" ||
        this.ruleForm.Phone == "";
      if (empty) {
        this.$message({
          type: "error",
          message: "输入信息不能为空！",
        });
      } else if (this.ruleForm.Password != this.ruleForm.CheckPassword) {
        this.$message({
          type: "error",
          message: "两次输入密码不一致！",
        });
      } else {
        this.options.forEach((item) => {
          if (item.value === this.selectedOptions[0]) {
            this.ruleForm.Province = item.label;
            console.log(item);
            item.children.forEach((item1) => {
              if (item1.value === this.selectedOptions[1]) {
                if (item1.label === "市辖区") {
                  this.ruleForm.City = item.label;
                } else {
                  this.ruleForm.City = item1.label;
                }
                item1.children.forEach((item2) => {
                  if (item2.value === this.selectedOptions[2]) {
                    this.ruleForm.Area = item2.label;
                  }
                });
              }
            });
          }
        });
        this.$axios
          .post("/hotel/register", paramsToFormData(this.ruleForm))
          .then((res) => {
            console.log(res)
            if (res?.code == "2000") {
              this.$message({
                type: "success",
                message: `${res?.message}`,
              });
              this.$router.push("/login");
            } else {
              this.$message({
                type: "error",
                message: `${res?.message}`,
              });
            }
          })
          .catch((err) => {
            this.$message({
              type: "error",
              message: `${err}`,
            });
          });
      }
    },
  },
};
</script>

<style scoped>
.register {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #fff;
  background-image: url("../assets/images/undraw_apartment_rent_o0ut.svg");
  background-size: 100% 100%;
}
.register .box {
  width: 450px;
  background: #d3dce6;
  border-radius: 5px;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  flex-direction: column;
  box-shadow: 0px 0px 5px #d3dce6;
}
.register .box .head {
  width: 120px;
  height: 120px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  background: #d3dce6;
  box-shadow: 0px 0px 5px #eee;
  transform: translateY(-50%);
}
.register .box .head img {
  width: 90%;
  height: 90%;
  border-radius: 50%;
  background: #fff;
}
</style>