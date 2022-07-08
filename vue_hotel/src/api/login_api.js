function login(){//管理员登录
        let empty = this.ruleForm.HotelAccount == "" ||this.ruleForm.Password == "";
        if(empty){
            this.$message({
                type:'error',
                message:'登录账号和密码不能为空！'
            })
        }else{
            this.$axios.get('/login',{
                params:{
                    HotelAccount:this.ruleForm.HotelAccount,
                    Password:this.ruleForm.Password,
                    userType:1
                }
            })
            .then(res =>{
                if(res.data.success){
                    this.$store.dispatch('setAdminInfo',res.data.admin);
                    this.$store.dispatch('setToken',res.data.token)
                    this.$router.push('/home');
                    this.$message({
                        type:'success',
                        message:'登录成功！'
                    })
                }else{
                    this.$message({
                        type:'error',
                        message:'登录失败！'
                    })
                }
            })
            .catch
        }
}