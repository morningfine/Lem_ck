import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'

Vue.use(VueRouter)

const routes = [{
		path: '/login',
		name: 'login',
		component: Login
	},
	{
		path: '/home',
		name: 'home',
		component: () => import('../components/Home.vue'),
		children: [{
			path: '/cases',
			name: 'cases',
			component: () => import('../components/Cases.vue'),
		}, {
			path: '/interface',
			name: 'interface',
			component: () => import('../components/Interface.vue'),
		}, {
			path: '/projects',
			name: 'peojects',
			component: () => import('../components/Projects.vue'),
		}, ]
	},
]

const router = new VueRouter({
	routes
})


// 添加路由导航守卫
// 除了login这个路由其他的路由都要进行了登录之后才能访问
router.beforeEach((to, from, next) => {
	// 判断访问的是否是登录页面
	// if (to.path === '/login') {
	// 	return next()
	// 	// 判断当前sessionStorage中是否有token(判断是否登录过)
	// } else if (window.sessionStorage.getItem('token')) {
	// 	return next()
	// } else {
	// 	return next('/login')
	// }
	if(to.path ==='/login'||window.sessionStorage.getItem('token')) return next()
	return next('/login')
	
})


export default router
