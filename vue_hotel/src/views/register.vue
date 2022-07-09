<template>
  <div class="register">
    <el-form
      :model="ruleForm"
      status-icon
      :rules="rules"
      ref="ruleForm"
      label-width="100px"
      class="demo-ruleForm"
    >
      <el-form-item label="" prop="type">
    <el-radio-group v-model="ruleForm.type">
        <el-radio :label="1">用户</el-radio>
        <el-radio :label="2">酒店</el-radio>
    </el-radio-group>
      </el-form-item>
      <el-form-item label="" prop="name">
        <el-input placeholder="名称" type="text" v-model="ruleForm.name" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="" prop="phone">
        <el-input placeholder="电话号码" type="text" v-model="ruleForm.phone" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="" prop="name2">
        <el-input placeholder="昵称" type="text" v-model="ruleForm.name2" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="" prop="email">
        <el-input placeholder="邮箱" type="text" v-model="ruleForm.email" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="" prop="password">
        <el-input placeholder="密码" type="password" v-model="ruleForm.password" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="" prop="">
        <el-button @click="submitForm('ruleForm')">注册</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
import * as Api from '@/request/api.js'
export default {
  data() {
    var checkEmpty = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('不能为空'));
      } else {
         callback();
      }
    };
    return {
      ruleForm: {
        type: 1,
        name:'',
        phone:'',
        name2:'',
        email:'',
        password:''
      },
      rules: {
        type: [{ validator: checkEmpty, trigger: 'blur' }],
        name: [{ validator: checkEmpty, trigger: 'blur' }],
        phone: [{ validator: checkEmpty, trigger: 'blur' }],
        name2: [{ validator: checkEmpty, trigger: 'blur' }],
        email: [{ validator: checkEmpty, trigger: 'blur' }],
        password: [{ validator: checkEmpty, trigger: 'blur' }],
      },
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(async (valid) => {
        if (valid) {
            if(this.ruleForm.type == 1) {
                const { name: UserName,phone:Phone,email:Email,password:Password} = this.ruleForm
                const params = {
                    UserName,
                    Phone,
                    Email,
                    Password,
                    Pic:''
                }
                console.log(params)
                // return
                const res = await Api.registerUser(params)
                if(res.code == 2000) {
                    this.$message({
                        message: '注册成功',
                        type: 'success'
                    });
                    this.$router.push({
                        path:'login'
                    })
                } else {
                    this.$message.error('注册失败');
                }
            } else {
                const { name: HotelName,phone:Phone,email:Email,password:Password,name2:HotelAccount} = this.ruleForm
                const params = {
                    HotelName,
                    Phone,
                    Email,
                    Password,
                    Province: "北京市", 
                    City: "北京市", 
                    Area: "昌平区", 
                    Address: "北农路2号华北电力大学", 
                    HotelAccount
                }
                const res = await Api.registerHotel(params)
                console.log(res)
                if(res.code == 2000) {
                    this.$message({
                        message: '注册成功',
                        type: 'success'
                    });
                    this.$router.push({
                        path:'login'
                    })
                } else {
                    this.$message.error('注册失败');
                }
            }
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    }
  },
};
</script>
<style lang="less">
.register{
        box-sizing: border-box;
        padding: 48px 24px;
     .demo-ruleForm {
        width: 50vw;
        margin: 0 auto;
        border: 2px solid black;
        border-radius: 8px;
        .el-form-item {
            .el-form-item__content{
                .el-input{
                    .el-input__inner{
                        width: 350px;
                    }
                }
            }
        }
    }
}
</style>