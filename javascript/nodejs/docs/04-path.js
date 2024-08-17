const path = require('path');
const fs = require('fs');

// path.join([..paths])
const pathStr = path.join('/a', '/b/c', '..', './d', '/e');
console.log("pathStr: ", pathStr);

const pathStr2 = path.join(__dirname, './temp/03-readFile.txt');
console.log("pathStr2: ", pathStr2);

/*
* 读文件的方法
* */
fs.readFile(pathStr2, 'utf8', (err, dataStr) => {
  if (err) {
    return console.log('读取文件失败！' + err.message);
  }
  console.log('读取文件成功！' + dataStr);
});


// path.basename() 
const fpath = 'a/b/c/index.html'
const FullFileName = path.basename(fpath)
console.log("FullFileName: ", FullFileName);

const FileName = path.basename(fpath, '.html')
console.log("FileName: ", FileName);


// path.extname()
const fpath2 = 'a/b/c/index.html5'
const extname = path.extname(fpath2);
console.log("extname: ", extname)


/*
* 综合案例：时钟案例
* */