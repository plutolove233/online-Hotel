<template>
    <div class="login">
        <div class="box">
            <div class="head">
                <img src="../assets/images/undraw_late_at_night_23xk.svg" alt="">
            </div>
            <el-form :model="ruleForm" status-icon  ref="ruleForm" label-width="60px" :rules="rules">
                <el-form-item label="账号" prop="account">
                    <el-input v-model.trim="ruleForm.account" autocomplete="off"  clearable></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="password">
                    <el-input type="password" v-model="ruleForm.password" autocomplete="off" show-password></el-input>
                </el-form-item>
                <el-form-item label="类型" prop="userType">
                    <el-radio v-model="ruleForm.userType" label="0">住客</el-radio>
                    <el-radio v-model="ruleForm.userType" label="1">宾馆</el-radio>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="login">登录</el-button>
                    <el-button @click="resetForm">重置</el-button>
                    <el-button type="text" @click="toRegister">注册</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script>
import qs from 'qs'
export default {
    name:'Login',
    data(){
        return {
            ruleForm:{
                account:'',
                password:'',
                userType: '0' // 0 住客 1 宾馆管理员
            },
            rules:{
                account:[
                    { required:true, message:'请输入用户账号', trigger:'blur' }
                ],  
                password:[
                    { required:true, message:'请输入用户密码', trigger:'blur' }
                ],
                userType: [
                    { required:true, message:'请选择用户类型', trigger:'blur' }
                ]
            }
        }
    },
    methods:{
        toRegister:function(){//登录注册界面
            this.$router.push('/register')
        },
        resetForm:function(){//重置数据
            this.$refs.ruleForm.resetFields();
        },
        login:function(){//管理员登录
            let empty = this.ruleForm.account == "" || this.ruleForm.password == "";
            if(empty){
                this.$message({
                    type:'error',
                    message:'登录账号和密码不能为空！'
                })
            }else{
                this.$axios({
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded'},
                    url: '/login',
                    data: qs.stringify(this.ruleForm)
                }).then(res =>{
                    console.log(res)
                    if (res.code == "2000") {
                        this.$message({
                            type:'success',
                            message:'登录成功！'
                        })
                        localStorage.setItem("token",res.data?.token)
                        localStorage.setItem("userinfo",res.data?.user)
                        this.$router.push('/home');
                    } else {
                        this.$message({
                            type:'error',
                            message:'登录失败！'
                        })
                    }
                })
                .catch(err => {
                    console.log(err)
                })
            }
        }
    }
}
</script>

<style scoped>
    .login{
        width:100%;
        height:100%;
        display: flex;
        justify-content: center;
        align-items: center;
        background: #fff;
        background-image: url('../assets/images/undraw_Ordinary_day_3gk3.svg');
        background-size: 100% 100%;
    }
    .login .box{
        width:450px;
        background:#D3DCE6;
        border-radius:5px;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        flex-direction: column;
        box-shadow:0px 0px 5px #D3DCE6;
    }
    .login .box .head{
        width:120px;
        height:120px;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius:50%;
        background:#eee;
        box-shadow:0px 0px 5px #fff;
        transform: translateY(-50%);
    }
    .login .box .head img{
        width:90%;
        height:90%;
        border-radius:50%;
        background:#fff;
    }
</style>