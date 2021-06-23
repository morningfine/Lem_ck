<template>
	<div class="login_box" style="width: 600px;height: 400px; margin: 50px auto;text-align: center;">
		<el-card class="box-card">
			<h1>用 户 登 录</h1>
			<el-form ref="form" :model="formLogin" label-width="80px">
				<el-form-item label="账号">
					<el-input v-model="formLogin.username"></el-input>
				</el-form-item>
				<el-form-item label="密码">
					<el-input v-model="formLogin.password" type='password'></el-input>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" @click="loginHandle">点击登录</el-button>
				</el-form-item>
			</el-form>
		</el-card>
	</div>

</template>

<script>
	export default {
		data() {
			return {
				formLogin: {
					username: '',
					password: ''
				}
			}
		},
		methods: {
			// 点击登录之后，处理登录的方法
			loginHandle: async function() {
				// 请求登录接口
				console.log('请求登录接口')
				const response = await this.$request.post('/user/login/', this.formLogin)
				console.log(response)
				// 判断登录请求是否成功 
				if (response.status === 200) {
					this.$message({
						message: '登录成功',
						type: 'success'
					});
					window.sessionStorage.setItem('token', response.data.token)
					this.$router.push('/home')
				} else {
					this.$message.error('登录失败');
				}
			}
		}
	}
</script>

<style>
</style>
