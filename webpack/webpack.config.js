const path = require('path')    // 引入path模块
const htmlWebpackPlugin = require('html-webpack-plugin')    // 配置生成预览也的配置项
const autoprefixer = require('autoprefixer')    // 导入自动添加浏览器前缀的插件autoprefixer
const VueLoaderPlugin = require('vue-loader/lib/plugin')

const htmlPlugin = new htmlWebpackPlugin({  // 创建一个在内存中生成html页面的插件，生成实例对象
    template: path.join(__dirname, './src/index.html'), // 指定模板文件路径
    filename: 'index.html' // 指定生成文件的名称，该文件存在内存中，不在目录中显示
})

module.exports = {
    mode: 'development', // mode 用来指定构建模式
    entry: path.join(__dirname, './src/index.js'), // 指定入口文件
    output: {
        path: path.join(__dirname, './dist'), // 指定输出路径
        filename: 'bundle.js' // 指定输出文件名
    },
    plugins: [htmlPlugin, autoprefixer, new VueLoaderPlugin()],    // plugin 用来配置 webpack 打包时会用到的一些插件
    // 所有第三方文件模块的匹配规则
    module: {
        rules: [
            { test: /\.css$/, use: ['style-loader', 'css-loader', 'postcss-loader'] },
            { test: /\.less$/, use: ['style-loader', 'css-loader', 'less-loader'] },
            { test: /\.scss$/, use: ['style-loader', 'css-loader', 'sass-loader'] },
            { test: /\.(jpg|png|gif|bmp|jpeg)$/, use: 'url-loader?limit=7631&name=[hash:8]-[name].[ext]' },
            { test: /\.js$/, exclude: /node_modules/, use: 'babel-loader'},
            { test: /\.vue$/, use: 'vue-loader'}
        ]
    }
}

