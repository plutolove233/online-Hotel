<template>
	<div class="login-register">
		<div class="contain">
			<div class="big-box" :class="{active:isLogin}">
				<div class="big-contain" key="bigContainLogin" v-if="isLogin">
					<div class="btitle">账户登录</div>
					<div class="bform">
						<input type="phuserphone" placeholder="电话号码/酒店账号" v-model="form.userphone">
						<span class="errTips" v-if="phuserphoneError">* 信息填写错误 *</span>
						<input type="password" placeholder="密码" v-model="form.userpwd">
						<span class="errTips" v-if="phuserphoneError">* 密码填写错误 *</span>
					</div>
					<button class="bbutton" @click="login">登录</button>
				</div>
				<div class="big-contain" key="bigContainRegister" v-else>
					<div class="btitle">创建账户</div>
					<div class="bform">
						<input type="text" placeholder="用户名" v-model="form.username">
						<span class="errTips" v-if="existed">* 用户已经存在！ *</span>
						<input type="phuserphone" placeholder="邮箱" v-model="form.userphone">
						<input type="password" placeholder="密码" v-model="form.userpwd">
					</div>
					<button class="bbutton" @click="register">注册</button>
				</div>
			</div>

			<div class="small-box" :class="{active:isLogin}">

				<div class="small-contain" key="smallContainRegister" v-if="isLogin">
					<div class="stitle">您好!</div>
					<p class="scontent">开始注册，共享云上酒店</p>
					<button class="sbutton" @click="changeType">注册</button>
				</div>
				<div class="small-contain" key="smallContainLogin" v-else>
					<div class="stitle">欢迎回来!</div>
					<p class="scontent">请登录您的账户</p>
					<button class="sbutton" @click="changeType">登录</button>
				</div>
			</div>
		</div>
	</div>
</template>


  <script lang="ts" setup>
  
  import {reactive } from 'vue'
  
  // do not use same name with ref
  const form = reactive({
	name: '',
	region: '',
	date1: '',
	date2: '',
	delivery: false,
	type: [],
	resource: '',
	desc: '',
  })
  
  const onSubmit = () => {
	console.log('submit!')
  }
  </script>
  
<script>
	export default{
		name:'login-register',
		data(){
			return {
				isLogin:false,
				userError: false,
				passwordError: false,
				existed: false,
				form:{
					username:'',
					userphone:'',
					userpwd:''
				}
			}
		},
		methods:{
			changeType() {
				this.isLogin = !this.isLogin
				this.form.username = ''
				this.form.userphone = ''
				this.form.userpwd = ''
			},
			login() {
				const self = this;
				if (self.form.userphone != "" && self.form.userpwd != "") {
					self.$axios({
						method:'post',
						url: 'http://127.0.0.1:10520/api/user/login',
						data: {
							phuserphone: self.form.userphone,
							password: self.form.userpwd
						}
					})
					.then( res => {
						switch(res.data){
							case 0: 
								alert("登陆成功！");
								break;
							case -1:
								this.phuserphoneError = true;
								break;
							case 1:
								this.passwordError = true;
								break;
						}
					})
					.catch( err => {
						console.log(err);
					})
				} else{
					alert("填写不能为空！");
				}
			},
			register(){
				const self = this;
				if(self.form.username != "" && self.form.userphone != "" && self.form.userpwd != ""){
					self.$axios({
						method:'post',
						url: 'http://127.0.0.1:10520/api/user/add',
						data: {
							username: self.form.username,
							phuserphone: self.form.userphone,
							password: self.form.userpwd
						}
					})
					.then( res => {
						switch(res.data){
							case 0:
								alert("注册成功！");
								this.login();
								break;
							case -1:
								this.existed = true;
								break;
						}
					})
					.catch( err => {
						console.log(err);
					})
				} else {
					alert("填写不能为空！");
				}
			}
		}
	}
</script>

<style scoped="scoped">
	
	.login-register{
		width: 100vw;
		height: 100vh;
		/* background-image: url(../../image/83960.jpg); */
		/* box-sizing: border-box; */
	}

	.contain{
		width: 70%;
		height: 70%;
		position: relative;
		top: 50%;
		left: 50%;
		transform: translate(-50%,-50%);
		background-color:lightblue;
		border-radius: 30px;
		/* box-shadow: 0 0 3px #f0f0f0,
					0 0 6px #f0f0f0; */
	}
	.big-box{
		width: 50%;
		height: 100%;
		position: absolute;
		top: 0;
		left: 30%;
		transform: translateX(0%);
		transition: all 1s;
	}
	.big-contain{
		width: 100%;
		height: 100%;
		/* display: block; */
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	.btitle{
		font-size: 2em;
		font-weight: bold;
		color:white;
	}
	.bform{
		width: 100%;
		height: 40%;
		padding: 2em 0;
		display: flex;
		flex-direction: column;
		justify-content: space-around;
		align-items: center;
	}
	.bform .errTips{
		display: block;
		width: 50%;
		text-align: left;
		color: red;
		font-size: 0.7em;
		margin-left: 1em;
	}
	.bform input{
		width: 50%;
		height: 30px;
		border: none;
		outline: none;
		border-radius: 10px;
		padding-left: 2em;
		background-color: #f0f0f0;
	}
	.bbutton{
		width: 20%;
		height: 40px;
		border-radius: 24px;
		border: none;
		outline: none;
		background-color: rgb(57,167,176);
		color: #fff;
		font-size: 0.9em;
		cursor: pointer;
	}
	.small-box{
		width: 30%;
		height: 100%;
		background: linear-gradient(135deg,rgb(57,167,176),rgb(56,183,145));
		position: absolute;
		top: 0;
		left: 0;
		transform: translateX(0%);
		transition: all 1s;
		border-top-left-radius: inherit;
		border-bottom-left-radius: inherit;
	}
	.small-contain{
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	.stitle{
		font-size: 1.5em;
		font-weight: bold;
		color: #fff;
	}
	.scontent{
		font-size: 0.8em;
		color: #fff;
		text-align: center;
		padding: 2em 4em;
		line-height: 1.7em;
	}
	.sbutton{
		width: 60%;
		height: 40px;
		border-radius: 24px;
		border: 1px solid #fff;
		outline: none;
		background-color: transparent;
		color: #fff;
		font-size: 0.9em;
		cursor: pointer;
	}
	
	.big-box.active{
		left: 0;
		transition: all 0.5s;
	}
	.small-box.active{
		left: 100%;
		border-top-left-radius: 0;
		border-bottom-left-radius: 0;
		border-top-right-radius: inherit;
		border-bottom-right-radius: inherit;
		transform: translateX(-100%);
		transition: all 1s;
	}
</style>
