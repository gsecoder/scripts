<?php
// PHP 代码的单行注释
/**
 * 代码的多行注释
 */
$x=5;
$y=6;
$z=$x+$y;
echo $z;
echo "<br>";

# 全局变量
$xx=50;
$xx1=500;
 
function myTest(){
   echo PHP_EOL;
    $yy=100;
    echo "<p>测试函数内变量：</p>";

    echo "变量X的值为：$xx";    // 你会发现你去调用的时候调用不到
    // 想要全局变量在函数内被使用，需要将其定义为global
    global $xx1;
    echo "xx1由于被声明为global全局变量，所以在函数内部也是可以被访问到的：$xx1";

   echo PHP_EOL;
    echo "变量 yy 为: $yy";
}
echo "函数外部访问，是可以访问到的：$xx";
echo "<br>";
echo "函数内部的变量，是无法访问到的：$yy";

myTest();


/**
 * =================【超级全局变量】==================
 * PHP 将所有全局变量存储在一个名为 $GLOBALS[index] 的数组中。 index 保存变量的名称。这个数组可以在函数内部访问，也可以直接用来更新全局变量。
 *
 *  除了上面的全局变量外，PHP中预定义了几个超级全局变量（super globals） ，这意味着它们在一个脚本的全部作用域中都可用
 *      $GLOBALS        包含了全部变量的全局组合数组。变量的名字就是数组的键。
 *      $_SERVER        含了诸如头信息(header)、路径(path)、以及脚本位置(script locations)等等信息的数组。
 *                      这个数组中的项目由 Web 服务器创建。不能保证每个服务器都提供全部项目；
 *                      服务器可能会忽略一些，或者提供一些没有在这里列举出来的项目
 *      $_REQUEST       PHP $_REQUEST 用于收集HTML表单提交的数据。
 *                      使用超级全局变量 $_REQUEST 来收集表单中的 input 字段数据:
 *      $_POST          PHP $_POST 被广泛应用于收集表单数据，在HTML form标签的指定该属性："method="post"
 *      $_GET
 *      $_FILES
 *      $_ENV
 *      $_COOKIE
 *      $_SESSION
 */
echo "--------------全局&局部变量------------";
$f1 = 11;
$f11 = 111;
$f2 = 22;
$f22 = 222;
echo PHP_EOL;
// $GLOBALS
function varScopeFuc($f){
    // 参数是通过调用代码将值传递给函数的局部变量；参数是在参数列表中声明的，作为函数声明的一部分
    echo "传参参数的值为：$f";
    echo PHP_EOL;
    $inner1 = 1;
    echo "【Inner Var】函数内的变量作为局部变量，值为：$inner1";

   echo PHP_EOL;
    $GLOBALS['f2'] = $GLOBALS['f2'] + $GLOBALS['f1'];

    // 全局变量在函数内部被使用的话，必须被global定义
    global $f11, $f22;
    $f22 = $f11 + $f11;
}
varScopeFuc(1);
echo "同样的表达效果：$f2";
echo "全局变量在函数内部被使用的话，必须被global定义：$f22";
echo PHP_EOL;
echo "【Inner Var】函数内的变量作为局部变量，外部是访问不到的：$inner1";
echo PHP_EOL;
// $_SERVER
echo "PHP_SELF: ", $_SERVER['PHP_SELF'];
echo PHP_EOL;
echo "SERVER_NAME: ", $_SERVER['SERVER_NAME'];
echo PHP_EOL;
echo "HTTP_HOST: ", $_SERVER['HTTP_HOST'];
echo PHP_EOL;
echo "HTTP_REFERER: ", $_SERVER['HTTP_REFERER'];
echo PHP_EOL;
echo "HTTP_USER_AGENT: ", $_SERVER['HTTP_USER_AGENT'];
echo PHP_EOL;
echo "SCRIPT_NAME: ", $_SERVER['SCRIPT_NAME'];
echo PHP_EOL;
/***
 * <html>
    <body>
     
    <form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
    Name: <input type="text" name="fname">
    <input type="submit">
    </form>
     
    <?php 
    $name = $_REQUEST['fname']; 
    echo $name; 
    ?>
     
    </body>
    </html>
 */


/**
 * 当一个函数完成时，它的所有变量通常都会被删除。然而，有时候您希望某个局部变量不要被删除，可以声明变量时使用 static 关键字
 *
 */
echo PHP_EOL;    // 换行符
echo "--------------Static 作用域------------";
echo PHP_EOL;    // 换行符
function staticVarFuc(){
    echo "Static 作用域";
    static $x = 0;
    echo "staticVarFuc 局部变量x的值为：$x";
    $x++;
    echo PHP_EOL;    // 换行符
}
staticVarFuc();
staticVarFuc();
staticVarFuc();


/**
 * echo & print
 *  echo: 可以输出一个或多个字符串；使用的时候可以不用加括号，也可以加上括号： echo 或 echo()
 *  print： 只允许输出一个字符串，返回值总为 1；可以使用括号，也可以不使用括号： print 或 print()
 *  VS：echo 输出的速度比 print 快， echo 没有返回值，print有返回值1
 */
echo "--------------echo & print------------";
$text1 = "echo & print";
$txt2="RUNOOB.COM";
$cars=array("Volvo","BMW","Toyota");
echo $text1;
echo PHP_EOL;
print $text1;
echo PHP_EOL;
echo ("<h3>菜鸟教程的网址是：$txt2</h3>");
echo PHP_EOL;
print ("<h3>菜鸟教程的网址是：$txt2</h3>");
echo PHP_EOL;
echo "我的车的品牌是：{$cars[1]}";
echo PHP_EOL;
print "我的车的品牌是：{$cars[1]}";
echo PHP_EOL;


/**
 * ******PHP 数据类型******
 *      String（字符串）, Integer（整型）, Float（浮点型）, Boolean（布尔型）, Array（数组）, Object（对象）, NULL（空值）。
 *
 *  var_dump()：函数返回变量的数据类型和值
 */
/***
 * PHP中的字符串变量：字符串变量用于包含有字符的值。
 *  .           并置运算符 (.) 用于把两个字符串值连接起来
 *  strlen()：返回字符串的长度（字节数）
 *  strpos()：用于在字符串内查找一个字符或一段指定的文本；如果在字符串中找到匹配，该函数会返回第一个匹配的字符位置。如果未找到匹配，则返回 FALSE。
 */
$string = "这是个字符串变量";
echo "输出字符串";
echo $string;
echo PHP_EOL;
$text1 = "Hello";
$text2 = "PHP";
$text3 = $text1." ".$text2;
echo $text3;
echo PHP_EOL;
echo '新字符串的字节数为：', strlen($text3);
echo PHP_EOL;
echo "查找字符串的字符或文本：", strpos($text3, 'loo');
// PHP EOF：是一种在命令行shell（如sh、csh、ksh、bash、PowerShell和zsh）和程序语言（像Perl、PHP、Python和Ruby）里定义一个字符串的方法。
echo <<<EOF
    <p>结束需要独立一行且前后不能空格</p>
    <h1>我的第一个标题</h1>
EOF;
echo PHP_EOL;
/**
 * 整数（规则）：
 *      整数必须至少有一个数字 (0-9)
 *      整数不能包含逗号或空格
 *      整数是没有小数点的
 *      整数可以是正数或负数
 *      整型可以用三种格式来指定：十进制， 十六进制（ 以 0x 为前缀）或八进制（前缀为 0）
 */
echo "===整数===";
$x = 5985;
var_dump($x);
echo PHP_EOL;
$x = -345; // 负数
var_dump($x);
echo PHP_EOL;
$x = 0x8C; // 十六进制数
var_dump($x);
echo PHP_EOL;
$x = 047; // 八进制数
var_dump($x);
/**
 * 浮点数：
 *  浮点数是带小数部分的数字，或是指数形式。
 */
echo "===浮点数===";
$x = 10.365;
var_dump($x);
echo PHP_EOL;
$x = 2.4e3;
var_dump($x);
echo PHP_EOL;
$x = 8E-5;
var_dump($x);
echo PHP_EOL;
/**
 * 布尔型：布尔型可以是 true 或 false；通常用于条件判断
 */
$x = true;
$y = false;
var_dump($x);
var_dump($y);
/**
 * 数组：数组可以在一个变量中存储多个值
 */
$myCar = array("比亚迪", "宝马", "Tesla");
var_dump($myCar);
echo PHP_EOL;
/**
 * 对象：对象数据类型也可以用于存储数据。
 *  PHP中关于对象的声明：首先，你必须使用class关键字声明类对象。类是可以包含属性和方法的结构；
 *  关键字this就是指向当前对象实例的指针，不指向任何其他对象或类
 */
class Car {
    var $color;
    function __construct($color="white")
    {
        $this->color = $color;
    }
    function what_color(): string
    {
        return $this->color;
    }
}
/**
 * NULL值：表示变量没有值。NULL 是数据类型为 NULL 的值。NULL 值指明一个变量是否为空值。 同样可用于数据空值和NULL值的区别。
 */
$x="Hello PHP";
$x=null;
echo "x的值会被重赋值为null，为：$x";
var_dump($x);
/**
 * PHP 中类型比较
 *  松散比较：使用两个等号 == 比较，只比较值，不比较类型。
 *  严格比较：用三个等号 === 比较，除了比较值，也比较类型。
 */
echo PHP_EOL;
if(42 == "42"){
    echo "1、值相等";
}
echo PHP_EOL;
if (42 === "42"){
    echo "2、类型相等";
}else{
    echo "3、类型不相等";
}
echo PHP_EOL;
echo "-------比较PHP中的0、false、null------";
echo PHP_EOL;
echo '0 == false: ';
var_dump(0 == false);
echo PHP_EOL;
echo '0 === false: ';
var_dump(0 === false);
echo PHP_EOL;
echo '0 == null: ';
var_dump(0 == null);
echo PHP_EOL;
echo '0 === null: ';
var_dump(0 === null);
echo PHP_EOL;
echo '"0" == null: ';
var_dump("0" == null);
echo PHP_EOL;
echo '"0" == false: ';
var_dump("0" == false);
echo PHP_EOL;
echo '"0" === null: ';
var_dump("0" === null);
echo PHP_EOL;
echo 'false == null: ';
var_dump(false == null);
echo PHP_EOL;
echo 'false === null: ';
var_dump(false === null);


/***
 * *-*-*-*-*-*-*-*-*-*- PHP 常量 *-*-*-*-*-*-*-*-*-*-*-*
 *  常量值被定义后，在脚本的其他任何地方都不能被改变；常量在定义后，默认是全局变量，可以在整个运行的脚本的任何地方使用。
 *  设置常量，使用 define() 函数：bool define ( string $name , mixed $value [, bool $case_insensitive = false ] )
 *      name：必选参数，常量名称，即标志符。
 *      value：必选参数，常量的值。
 *      case_insensitive ：可选参数，如果设置为 TRUE，该常量则大小写不敏感。默认是大小写敏感的。
 * 
 *  可以把在类中始终保持不变的值定义为常量。在定义和使用常量的时候不需要使用 $ 符号
 *  常量的值必须是一个定值，不能是变量，类属性，数学运算的结果或函数调用。
 */
define("TALL", "170");
echo TALL;
echo PHP_EOL;
function constFuc() {
    echo TALL;
}
constFuc();
echo PHP_EOL;
/**
 * 魔术常量，PHP 向它运行的任何脚本提供了大量的预定义常量。
 * 很多常量都是由不同的扩展库定义的，只有在加载了这些扩展库时才会出现，或者动态加载后，或者在编译时已经包括进去了
 * 有八个魔术常量它们的值随着它们在代码中的位置改变而改变
 */
// __LINE__ 文件中的当前行号。
echo '这是第 " '  . __LINE__ . ' " 行';
echo PHP_EOL;
// __FILE__ 文件的完整路径和文件名。如果用在被包含文件中，则返回被包含的文件名。
echo '该文件位于： " '  . __FILE__ . ' " ';
echo PHP_EOL;
// __DIR__  文件所在的目录。如果用在被包括文件中，则返回被包括的文件所在的目录
echo '该文件所在目录： " '  . __DIR__ . ' " ';
echo PHP_EOL;
// __FUNCTION__  自 PHP5 起本常量返回该函数被定义时的名字（区分大小写）
function testFuc() {
    echo  '函数名为：' . __FUNCTION__ ;
}
testFuc();
echo PHP_EOL;
// __CLASS__  自 PHP5 起本常量返回该类被定义时的名字（区分大小写）
class testClass {
    function _print() {
        echo '类名为：'  . __CLASS__ . PHP_EOL;
        echo  '函数名为：' . __FUNCTION__ ;
    }
}
$t = new testClass();
$t->_print();
// __TRAIT__  实现了代码复用的一个方法，称为 traits;
echo PHP_EOL;
class Base {
    public function sayHello() {
        echo 'Hello ';
    }
}
 
trait SayWorld {
    public function sayHello() {
        parent::sayHello();
        echo 'World!';
    }
}
 
class MyHelloWorld extends Base {
    use SayWorld;
}
 
$o = new MyHelloWorld();
$o->sayHello();
echo PHP_EOL;
// __METHOD__  类的方法名（PHP 5.0.0 新加）。返回该方法被定义时的名字（区分大小写）。
function testMethod1() {
    echo  '函数名为：' . __METHOD__ ;
}
testMethod1();
/**
 *  __NAMESPACE__   当前命名空间的名称（区分大小写）
 * PHP 命名空间可以解决以下两类问题：
 *      用户编写的代码与PHP内部的类/函数/常量或第三方类/函数/常量之间的名字冲突。
 *      为很长的标识符名称(通常是为了缓解第一类问题而定义的)创建一个别名（或简短）的名称，提高源代码的可读性
 *  将全局的非命名空间中的代码与命名空间中的代码组合在一起，只能使用大括号形式的语法。全局代码必须用一个不带名称的 namespace 语句加上大括号括起来
 *  在声明命名空间之前唯一合法的代码是用于定义源文件编码方式的 declare 语句。所有非 PHP 代码包括空白符都不能出现在命名空间的声明之前
 */
//namespace MyProject;
//echo '命名空间为："', __NAMESPACE__, '"'; // 输出 "MyProject"



/***
 * PHP 运算符
 */
echo PHP_EOL;
$x1 = 100;
echo "x1先加1，然后返回x1：", ++$x1;
echo PHP_EOL;
$x2 = 100;
echo "先返回x2，再给x2加1：", $x2 ++;
echo PHP_EOL;
$x3 = 100;
echo "x3先减1，然后返回x3：", --$x3;
echo PHP_EOL;
$x4 = 100;
echo "先返回x3，再后x3减1：", $x3--;


/***
 * PHP 条件分支
 *  if 语句 - 在条件成立时执行代码
 *  if...else 语句 - 在条件成立时执行一块代码，条件不成立时执行另一块代码
 *  if...elseif....else 语句 - 在若干条件之一成立时执行一个代码块
 *  switch 语句 - 在若干条件之一成立时执行一个代码块
 */
$t=date("H");
echo $t;
if ($t<"20")
{
    echo "Have a good day!";
}
echo PHP_EOL;
$favcolor="red";
switch ($favcolor){
    case "red":
        echo "red...";
        break;
    case "yellow":
        echo "yellow...";
        break;
    case "green":
        echo "green";
        break;
    default:
        echo "All";
}


/***
 * PHP 数组：数组能够在单个变量中存储多个值
 *      数值数组 - 带有数字 ID 键的数组
 *      关联数组 - 带有指定的键的数组，每个键关联一个值
 *      多维数组 - 包含一个或多个数组的数组
 *
 *  count() 函数用于返回数组的长度（元素的数量）
 *
 */
echo PHP_EOL;
$cars=array("Volvo","BMW","Toyota");
echo "I like " . $cars[0] . ", " . $cars[1] . " and " . $cars[2] . ".";
echo PHP_EOL;
$fruit[0]='apple';
$fruit[1]='orange';
echo "I like " . $fruit[0] . ", " . $fruit[1];
echo PHP_EOL;
echo "长度为：", count($fruit);
echo "便利数组：";
for ($x=0; $x<count($cars); $x++){
    echo "元素分别是：", $cars[$x];
    echo PHP_EOL;
}
echo PHP_EOL;
// 关联数组创建&遍历
$age = array("A"=>12, "B"=>13, "C"=>14);
echo "小盆友 ".$age['A']." years old";
echo PHP_EOL;
foreach ($age as $x=>$x_value){
    echo "Key=" . $x . ", Value=" . $x_value;
    echo PHP_EOL;
}
// 多维数组
/**
 * 数组排序
 */
$friends = array("B"=>"Bb", "A"=>"Aa", "C"=>"Cc");
// sort() - 对数组进行升序排列
sort($friends);
print_r($friends);
// rsort() - 对数组进行降序排列
rsort($friends);
print_r($friends);
// asort() - 根据关联数组的值，对数组进行升序排列
asort($friends);
print_r($friends);
// ksort() - 根据关联数组的键，对数组进行升序排列
ksort($friends);
print_r($friends);
// arsort() - 根据关联数组的值，对数组进行降序排列
arsort($friends);
print_r($friends);
// krsort() - 根据关联数组的键，对数组进行降序排列
krsort($friends);
print_r($friends);


/***
 * -*-*-*-*-*-*-*-*-*-*-*-*-*-*-* PHP 循环 *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- 
 */
/**
 * while循环：
 *      while - 只要指定的条件成立，则循环执行代码块
 *      do...while - 首先执行一次代码块，然后在指定的条件成立时重复这个循环
 */
$i1=1;
while ($i1<5){
    echo "1、The number is: ", $i1;
    $i1++;
    echo PHP_EOL;
}
echo PHP_EOL;
$i2=1;
do{
   $i2++;
   echo "2、The number is: ", $i2;
   echo PHP_EOL;
}
while($i2<5);
/**
 *  for循环：
 *      for - 循环执行代码块指定的次数
 *      foreach - 循环用于遍历数组；根据数组中每个元素来循环代码块
 */
echo PHP_EOL;
for($i3=0; $i3<=5; $i3++){
    echo "i3的值为：", $i3;
    echo PHP_EOL;
}
echo PHP_EOL;
$i4=array("A1"=>11, "B1"=>21, "C1"=>31);
foreach ($i4 as $item => $value){
    echo "key为：".$item."，value为：", $value.PHP_EOL;
}


/***
 * -*-*-*-*-*-*-*-*-*-*-*-*-*-*-* PHP 函数 *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- 
 */
/**
 * PHP 内建函数
 */
// 
/**
 * PHP 自定义函数
 *      函数的名称应该提示出它的功能
 *      函数名称以字母或下划线开头（不能以数字开头）
 *  函数参数就在函数名称后面的一个括号内指定
 *  如需让函数返回一个值，请使用 return 语句
 */
echo PHP_EOL;
function addition($x, $y){
    /** @var TYPE_NAME $z */
    $z = $x + $y;
    return $z;
}
echo "1 + 2 = ", addition(1, 2);