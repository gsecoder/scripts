/**
 * Buffer 创建的三种方式
 * */

/**方式一：alloc创建的缓存空间归 0，是个新空间*/
let buf1 = Buffer.alloc(10);
console.log("buf1: ", buf1);  // buf1: <Buffer 00 00 00 00 00 00 00 00 00 00>


/**方式二：allocUnsafe创建的缓存空间存在上一次程序的旧的内存数据；这种方式相比于 alloc 创建速度快一些*/
let buf2 = Buffer.allocUnsafe(10);
console.log("buf2: ", buf2);  // buf2:  <Buffer 00 00 00 00 00 00 00 00 00 00>

/**方式三：from 将字符对应的 Unicode 码存储到缓存中*/
let buf3 = Buffer.from("hello");
console.log("buf3: ", buf3);    // buf3:  <Buffer 68 65 6c 6c 6f>
let buf4 = Buffer.from([1, 2, 3, 4, 5, 22, 33]);
console.log("buf4: ", buf4);    // buf4:  <Buffer 01 02 03 04 05 16 21>


/**
 * Buffer 与字符串的转换
 * */
let buf_str = Buffer.from([105, 108, 111, 118, 101, 121, 111, 117]);
console.log("buf_str: ", buf_str.toString());  // buf_str:  iloveyou

/**
 * Buffer 的读写
 * */
let buf_read = Buffer.from("Hello");
// 读取 buffer 中的字符
console.log("buf_read_0: ", buf_read[0]) ;     // buf_read_0:  72
// 读取 buffer 中的字符，并转换为二进制
console.log("buf_read_to2: ", buf_read[0].toString(2)); // buf_read_to2:  1001000
// 修改 buffer 中的字符串，修改前的 buffer 数据为
console.log("buf_read_bef: ", buf_read);    // buf_read_bef:  <Buffer 48 65 6c 6c 6f>
// 修改 buffer 中的字符串，修后前的 buffer 数据为
buf_read[0] = 99;
console.log("buf_read_aft: ", buf_read);    // buf_read_aft:  <Buffer 63 65 6c 6c 6f>
console.log("buf_read_toStr: ", buf_read.toString());   // buf_read_toStr:  cello


/**
 * Buffer 的溢出
 * */
let buf_stack = Buffer.from("Hello");
buf_stack[0] = 361; // 二进制最高存储 256，会舍弃高位的数字：0001 0110 1001 ==> 0110 1001
console.log("buf_stack_toString: ", buf_stack.toString())   // buf_stack_toString:  iello

/**
 * Buffer 的中文显示
 * */
let buf_cn = Buffer.from("中文");
console.log("buf_cn: ", buf_cn); 
let buf_en = Buffer.from("Hello");  // buf_cn:  <Buffer e4 b8 ad e6 96 87>
console.log("buf_en: ", buf_en);    // buf_en:  <Buffer 48 65 6c 6c 6f>
