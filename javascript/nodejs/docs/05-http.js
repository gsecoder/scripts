// 导入http模块
const http = require('http');

// 创建 web 服务器实例
const server = http.createServer();

// 为服务器绑定request 事件，处理客户端请求
server.on('request', (req, res) => {
    console.log('Someone visit our web server.')
    const url = req.url // 请求地址
    const method = req.method // 请求url
    
    // 根据路径判断返回不同内容
    let content = '<h1>404 Not found!</h1>'
    if(url === '/' || url === '/index.html') {
        content = '<h1>首页</h1>' +
            '<h2>自定义</h2>'
    }
    
    res.setHeader('Content-Type', 'text/html; charset=utf-8') // 设置响应头
    res.end(content) // 向客户端响应内容
})

// 启动服务器
server.listen(80, () => {
    console.log('http server running at http://127.0.0.1')
})
