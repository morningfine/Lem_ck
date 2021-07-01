<template>
	<div class="caseEdit">
		<el-card class="box-card">
			<!-- 顶部的面包屑 -->
			<div slot="header" class="clearfix">
				<el-breadcrumb separator-class="el-icon-arrow-right">
					<el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
					<el-breadcrumb-item>用例管理</el-breadcrumb-item>
					<el-breadcrumb-item>用例编辑</el-breadcrumb-item>
				</el-breadcrumb>
			</div>
			<!-- 显示主体内容的卡片 -->
			<el-card class="box-card">
				<el-divider content-position="left"><span style="color: #409EFF; font-weight: bold;">Api</span>
				</el-divider>
				<!-- api请求的基本信息 -->
				<el-row :gutter="20">
					<!-- 请求方法选择 -->
					<el-col :span="3">
						<el-select v-model="caseInfo.method" placeholder="请求方法">
							<el-option label="GET" value="GET"></el-option>
							<el-option label="POST" value="POST"></el-option>
							<el-option label="PUT" value="PUT"></el-option>
							<el-option label="DELETE" value="DELETE"></el-option>
							<el-option label="PATCH" value="PATCH"></el-option>
							<el-option label="HEAD" value="HEAD"></el-option>
							<el-option label="OPTION" value="OPTION"></el-option>
						</el-select>
					</el-col>
					<!-- host地址输入 -->
					<el-col :span="9">
						<el-input placeholder="host地址" v-model="caseInfo.host">
							<template slot="prepend">Host</template>
						</el-input>
					</el-col>
					<!-- 接口地址输入 -->
					<el-col :span="9">
						<el-input placeholder="接口路径" v-model="caseInfo.interface">
							<template slot="prepend">接口地址</template>
						</el-input>
					</el-col>
					<!-- 运行按钮 -->
					<el-col :span="3">
						<el-button type="primary" icon="el-icon-s-promotion">Run</el-button>
					</el-col>
				</el-row>
				<el-divider content-position="left"><span style="color: #409EFF; font-weight: bold;">Request</span>
				</el-divider>
				<!--用例信息 -->
				<el-tabs type="border-card">
					<!-- 请求头 -->
					<el-tab-pane label="请求头">
						<el-row :gutter="20" v-for='header in caseInfo.headers' :key='header.key' style="margin: 10px;">
							<el-col :span="6">
								<el-input v-model.lazy="header.key" placeholder="KEY"></el-input>
							</el-col>
							<el-col :span="12">
								<el-input v-model.lazy="header.value" placeholder="VALUE"></el-input>
							</el-col>
							<el-col :span="6">
								<el-button type="danger" icon="el-icon-delete" @click='deleteRow(header)'></el-button>
							</el-col>
						</el-row>
					</el-tab-pane>
					<!-- 请求参数 -->
					<el-tab-pane label="请求参数">
						<el-tabs>
							<el-tab-pane label="application/json" name="second">
								<editor height="300" width="100%" ref="editor" :content="caseInfo.json"
								    v-model="caseInfo.json" :options="{
								    enableBasicAutocompletion: true,
								    enableSnippets: true,
								    enableLiveAutocompletion: true,
								    tabSize:2,
								    fontSize:20,
								    showPrintMargin:false,}" :lang="'json'" @init="editorInit">
								</editor>
							</el-tab-pane>
							<el-tab-pane label="Params" name="first">查询字符串参数</el-tab-pane>
							<el-tab-pane label="application/X-www-urlencode" name="third">表单参数</el-tab-pane>
						</el-tabs>

					</el-tab-pane>
					<el-tab-pane label="响应提取">响应提取</el-tab-pane>
					<el-tab-pane label="用例断言">用例断言</el-tab-pane>
					<el-tab-pane label="数据库校验">数据库校验</el-tab-pane>
				</el-tabs>

			</el-card>
		</el-card>

	</div>
</template>

<script>
	import Editor from 'vue2-ace-editor'
	
	export default {
		data() {
			return {
				caseInfo: {
					method: 'GET',
					host: '',
					interface: '',
					headers: [{
						key: '',
						value: ''
					}],
					params:[{
						key: '',
						value: ''
					}],
					data:[{
						key: '',
						value: ''
					}],
					json:'{}'
				}
			}
		},
		methods: {
			deleteRow(header) {
				console.log(header)
				// 删除一行内容
				const newHeaders = this.caseInfo.headers.filter(function(item, index) {
					return item !== header
				})
				this.caseInfo.headers = newHeaders
			},
			editorInit() {
			    require('brace/theme/chrome')
			    require('brace/ext/language_tools')
			    require('brace/mode/yaml')
			    require('brace/mode/json')
			    require('brace/mode/less')
			    require('brace/snippets/json')
			}
		},
		watch: {
			// 监听headers中的数据是否发送变化，当发送变化时，则判断最后一行是否有值，
			'caseInfo.headers': {
				handler: function(value, oldVal) {
					if (value.length === 0) {
						this.caseInfo.headers.push({
							key: '',
							value: ''
						})
					}
					// 判断最后一行是否有值，
					if (value[value.length - 1].key || value[value.length - 1].value) {
						this.caseInfo.headers.push({
							key: '',
							value: ''
						})
					}

				},
				deep: true
			}

		},
		components:{
			Editor
		}
		
		



	}
</script>

<style scoped>
</style>
