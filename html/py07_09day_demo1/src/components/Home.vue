<template>
	<div>
		<div>
			<el-menu :router='rou' background-color='#555500' class="el-menu-demo" mode="horizontal"
				default-active='/cases' text-color="#fff" active-text-color="#00aaff">
				<el-menu-item index="/cases">用例列表</el-menu-item>
				<el-menu-item index="/interface">接口列表</el-menu-item>
				<el-menu-item index="/projects">项目列表</el-menu-item>
			</el-menu>
			<router-view></router-view>
		</div>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				rou: true
			}
		}
	}
</script>

<style>
</style>
