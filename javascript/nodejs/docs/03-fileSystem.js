/**fs 模块*/

/**fs.writeFile异步写入*/
// 1、导入fs 模块【require 是 node.js 环境中的全局变量，用来导入模块】
const fs1 = require('fs');
// 2、写入文件
fs1.writeFile('./temp/03-fileSystem.txt', '三人行，必有我师焉～', err=>{
    if (err){
        console.log('写入失败');
        return;
    }
    console.log("写入成功");
})

/**fs.writeFileSync同步写入*/
// 1、导入fs 模块【require 是 node.js 环境中的全局变量，用来导入模块】
const fs2 = require('fs');
// 2、写入文件
fs2.writeFileSync('./temp/03-fileSystem2.txt', '3人行，必有我师焉2ceshi', err=>{
    if (err){
        console.log('写入失败');
        return;
    }
    console.log("写入成功");
})


/**fs.appendFile同步写入*/
// 1、导入fs 模块【require 是 node.js 环境中的全局变量，用来导入模块】
const fs3 = require('fs');
// 2、调用appendFile
fs3.appendFile('./temp/03-fileSystem.txt', '择其善者而从之，其不善者而改之', err=>{
    if (err){
        console.log('追加失败');
        return;
    }
    console.log("追加成功");
})
const fs4 = require('fs');
fs4.appendFileSync('./temp/03-fileSystem2.txt', '\r\n温故而知新', err=>{
    if (err){
        console.log('追加失败');
        return;
    }
    console.log("追加成功");
})
const fs5 = require('fs');
fs5.writeFile('./temp/03-fileSystem2.txt', '\r\n温故而知新2', {flag: "a"}, err=>{
    if (err){
        console.log('追加失败');
        return;
    }
    console.log("追加成功");
})

/**fs.createWriteStream流式写入*/
// 1、导入 fs
const fs6 = require('fs');
// 2、创建写入流对象
const ws = fs6.createWriteStream('./temp/03-createWriteStream.txt');
// 3、写入流式数据
ws.write("半亩方塘一鉴开")
ws.write("\r\n天光云彩共徘徊")
ws.write("\r\n问渠那得清如许")
ws.write("\r\n为有源头活水来")
// 4、关闭流式通道
ws.close()


/**
 * 文件读取
 * */
/**fs.readFile异步读取文件*/
// 1、引入 fs 模块
const fs_readFile = require('fs');
// 2、异步读取文件数据
fs_readFile.readFile('./temp/03-readFile.txt', (err, data)=>{
    if(err){
        console.log("文件读取失败");
        return;
    }
    console.log(data.toString())
})

/**fs.readFileSync同步读取文件*/
// 1、引入 fs 模块
const fs_readFileSync = require('fs');
// 2、同步读取文件数据
let  data = fs_readFileSync.readFileSync('./temp/03-readFile.txt');
console.log("data: ", data.toString())


/**fs.createReadStream：流式读取*/
// 1、引入 fs 模块
const fs_createReadStream = require('fs');
// 2、流式读取文件数据
const fs_crs = fs_createReadStream.createReadStream('./temp/03-createReadStream.mp4');
fs_crs.on('data', chunk=>{
    console.log("chunk: ", chunk)
    console.log("chunk.length: ", chunk.length)
})
fs_crs.on('end', ()=>{
    console.log("读取完成✅")
})
/**流式读取案例*/



/**
 * 文件复制
 * */
// 方式一：读取文件，再写入新文件
// 1、导入 fs
const fs_copy1 = require('fs')
// 2、读取文件
let data_copy = fs_copy1.readFileSync('./temp/03-createWriteStream.txt');
// 3、写入新文件
fs_copy1.writeFileSync('./temp/03-createWriteStream-copy.txt', data_copy);
console.log("process.memoryUsage()--1: ", process.memoryUsage())

// 方式二：读取文件，再写入新文件，不过使用流式操作；更推荐这个方式复制，理想条件下每次只去 64kb 完成数据的读取写入
// 1、导入 fs
const fs_copy2 = require('fs')
// 2、读取文件流对象
const fs_copy_crs = fs_copy2.createReadStream('./temp/03-createWriteStream.txt');
// 3、写入文件流对象
const  fs_copy_cws = fs_copy2.createWriteStream('./temp/03-createWriteStream-copyStream.txt')
// 4、绑定 data 事件
fs_copy_crs.on('data', chunk=>{
    fs_copy_cws.write(chunk)
})
fs_copy_crs.on('end', ()=>{
    console.log("process.memoryUsage()--2: ", process.memoryUsage())
})

// 方式三：pipe
fs_copy_crs.pipe(fs_copy_cws)


/**
 *  fs 文件移动/重命名
 * */
// 1、导入 fs
const fs_rename = require('fs')
// 调用 rename 方法
fs_rename.rename('./temp/03-createWriteStream-rename.txt', './temp/03-createWriteStream-rename2.txt', err=>{
    if(err){
        console.log("重命名失败")
    }
    console.log("重命名成功")
})


/**
 *  fs 文件删除
 * */
// 1、导入 fs
const fs_unlink = require('fs')
// 2、调用 unlink
fs_unlink.unlink('./temp/03-createWriteStream-rename2.txt', err => {
    if(err){
        console.log("文件删除失败")
    }
    console.log("文件删除成功")
})


/**
 *  fs 文件夹操作
 * */

/**文件夹创建*/
const fs_mkdir = require('fs')
// recursive: true 递归创建，默认不写也是可以的
fs_mkdir.mkdir('./temp/mkdir_dir/a', {recursive: true},err=>{
    if(err){
        console.log("创建文件夹失败")
    }
    console.log("创建文件夹成功")
})

/**文件夹读取*/
const fs_readdir = require('fs')
fs_readdir.readdir('./temp', (err, data)=>{
    if(err){
        console.log("读取文件夹失败")
    }
    console.log("读取文件夹成功data：", data)
})
// 批量重命名
const fs_readdir_more = require('fs')
const files = fs_readdir_more.readdirSync('./temp')
files.forEach(item=>{
    let data = item.split('-');
    let[num, name] = data;
    if(Number(num)<10){
        num = '0' + num
    }
    let newName = num + '-' + name;
    fs_readdir_more.readdirSync(`./tem/${item}`, `./tem/${newName}`)
})

/**删除文件夹*/
const fs_rmdir = require('fs')
fs_rmdir.rmdir('./temp/c', {recursive: true},err => {
    if(err){
        console.log("删除文件夹失败")
    }
    console.log("删除文件夹成功")
})


/**查看资源状态*/
const fs_stat = require('fs')
fs_stat.stat('./temp/03-createReadStream.mp4', (err, data)=>{
    if(err){
        console.log("获取文件状态失败");
        return
    }
    console.log("获取文件状态成功data：", data)
    console.log("isFile：", data.isFile())
    console.log("isDirectory：", data.isDirectory())
})


/**
 * fs 路径相关：
 *  __dirname：全局变量，保存的是所在文件所在目录的绝对路径
 * */
console.log("__dirname: ", __dirname)


