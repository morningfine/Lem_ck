const express = require('express')
// 创建一个应用程序对象
const app = express()
// 指定静态资源的路径
app.use(express.static('./dist'))
// 指定监听端口

app.listen(80,()=>{
	console.log('服务已启动，运行在127.0.0.1:80端口')
})
