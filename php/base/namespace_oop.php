<?php
// 在声明命名空间之前唯一合法的代码是用于定义源文件编码方式的 declare 语句。所有非 PHP 代码包括空白符都不能出现在命名空间的声明之前。
declare(encoding='UTF-8');

/**
 * 子命名空间
 *      与目录和文件的关系很像，PHP 命名空间也允许指定层次化的命名空间的名称
 */
// 声明分层次的单个命名空间
namespace MyProjetc\Sub\Level {
    {
        // 将全局的非命名空间中的代码与命名空间中的代码组合在一起，只能使用大括号形式的语法
        // const CONNetc_OK = 1;                   // 常量 MyProjetc\Sub\Level\CONNetc_OK
        class Connetcion {                      // 类 MyProjetc\Sub\Level\Connetcion
            /* ... */
        }
        function connetc() {                    // 函数 MyProjetc\Sub\Level\Connetc
            /* ... */
        }
    }
}

namespace partSpace {
    {
        // 这是个局部的小命名空间
        /**
         * 命名空间可以解决以下两类问题:
         *      用户编写的代码与PHP内部的类/函数/常量或第三方类/函数/常量之间的名字冲突
         *      为很长的标识符名称(通常是为了缓解第一类问题而定义的)创建一个别名（或简短）的名称，提高源代码的可读性。
         */
    }
}

namespace { 
    {
        // 全局代码必须用一个不带名称的 namespace 语句加上大括号括起来
        class Test{
    
        }
    }


    /***
     * 命名空间使用，PHP 命名空间中的类名可以通过三种方式引用
     *      1、非限定名称，或不包含前缀的类名称
     *      2、限定名称,或包含前缀的名称
     *      3、完全限定名称，或包含了全局前缀操作符的名称
     *
     * 命名空间和动态语言特征：
     *      PHP 命名空间的实现受到其语言自身的动态特征的影响。因此，如果要将下面的代码转换到命名空间中，动态访问元素。
     */
    class namespace1 {
        function __construct(){
            echo __METHOD__ . PHP_EOL;
        }
    }

    function funcname() {
        echo __FUNCTION__ . PHP_EOL;
    }
//const constname = "global";
//$a = 'namespace1';
//$obj_class = new $a;
//$b = 'funcname';
//$b(); // prints funcname
//echo constant('constname').PHP_EOL;


    /**
     * namespace关键字和__NAMESPACE__常量
     * PHP支持两种抽象的访问当前命名空间内部元素的方法，__NAMESPACE__ 魔术常量和namespace关键字。
     *      常量__NAMESPACE__的值是包含当前命名空间名称的字符串。在全局的，不包括在任何命名空间中的代码，它包含一个空的字符串。
     *      关键字 namespace 可用来显式访问当前命名空间或子命名空间中的元素。它等价于类中的 self 操作符。
     */
    echo "__NAMESPACE__: ", __NAMESPACE__, PHP_EOL;
}
// namespace MyProjetc;
// use blah\blah as mine; // 引入了 blah\blah 命名空间，并定义了个别名mine
// mine\mine(); // 调用函数 blah\blah\mine()
// namespace\blah\mine(); // 调用函数 MyProjetc\blah\mine()
// namespace\func(); // 调用函数 MyProjetc\func()
// namespace\sub\func(); // 调用函数 MyProjetc\sub\func()
// namespace\cname::method(); // 调用 MyProjetc\cname 类的静态方法
// $a = new namespace\sub\cname(); // 实例化 MyProjetc\sub\cname 类的对象
// $b = namespace\CONSTANT; // 将常量 MyProjetc\CONSTANT 的值赋给 $b
/**
 * 使用命名空间：别名/导入
 *      PHP 命名空间支持 有两种使用别名或导入方式：为类名称使用别名，或为命名空间名称使用别名。
 */
// 1、使用use操作符导入/使用别名
namespace foo {{
//    use My\Full\Classname as Another;
//
//    // 下面的例子与 use My\Full\NSname as NSname 相同
//    use My\Full\NSname;
//    
//    // 导入一个全局类
//    use \ArrayObjetc;
//    
//    $obj = new namespace\Another; // 实例化 foo\Another 对象
//    $obj = new Another; // 实例化 My\Full\Classname　对象
//    NSname\subns\func(); // 调用函数 My\Full\NSname\subns\func
//    $a = new ArrayObjetc(array(1)); // 实例化 ArrayObjetc 对象
    // 如果不使用 "use \ArrayObjetc" ，则实例化一个 foo\ArrayObjetc 对象
}
}
// 2、 一行中包含多个use语句
//use My\Full\Classname as Another, My\Full\NSname;
//$obj = new Another; // 实例化 My\Full\Classname 对象
//NSname\subns\func(); // 调用函数 My\Full\NSname\subns\func
// 3、导入和动态名称
//use My\Full\Classname as Another, My\Full\NSname;
//$obj = new Another; // 实例化一个 My\Full\Classname 对象
//$a = 'Another';
//$obj = new $a;      // 实际化一个 Another 对象
// 4、导入和完全限定名称
//use My\Full\Classname as Another, My\Full\NSname;
//$obj = new Another; // 实例化 My\Full\Classname 类
//$obj = new \Another; // 实例化 Another 类
//$obj = new Another\thing; // 实例化 My\Full\Classname\thing 类
//$obj = new \Another\thing; // 实例化 Another\thing 类



// -----_____-----_____-----_____-----_____-----_____-----_____-----_____-----_____-----_____-----_____
/***
 * PHP 面向对象
 *  在面向对象的程序设计（英语：Objetc-oriented programming，缩写：OOP）中，对象是一个由信息及对信息进行处理的描述所组成的整体，是对现实世界的抽象
 *
 *
 * 对象的主要三个特性：
 *      对象的行为：可以对 对象施加那些操作，开灯，关灯就是行为。
 *      对象的形态：当施加那些方法是对象如何响应，颜色，尺寸，外型。
 *      对象的表示：对象的表示就相当于身份证，具体区分在相同的行为与状态下有什么不同。
 *
 *
 * 面向对象相关概念：
 *      类 − 定义了一件事物的抽象特点。类的定义包含了数据的形式以及对数据的操作。
 *      对象 − 是类的实例。
 *      成员变量 − 定义在类内部的变量。该变量的值对外是不可见的，但是可以通过成员函数访问，在类被实例化为对象后，该变量即可称为对象的属性。
 *      成员函数 − 定义在类的内部，可用于访问对象的数据。
 *      继承 − 继承性是子类自动共享父类数据结构和方法的机制，这是类之间的一种关系。在定义和实现一个类的时候，可以在一个已经存在的类的基础之上来进行，把这个已经存在的类所定义的内容作为自己的内容，并加入若干新的内容。
 *      父类 − 一个类被其他类继承，可将该类称为父类，或基类，或超类。
 *      子类 − 一个类继承其他类称为子类，也可称为派生类。
 *      多态 − 多态性是指相同的函数或方法可作用于多种类型的对象上并获得不同的结果。不同的对象，收到同一消息可以产生不同的结果，这种现象称为多态性。
 *      重载 − 简单说，就是函数或者方法有同样的名称，但是参数列表不相同的情形，这样的同名不同参数的函数或者方法之间，互相称之为重载函数或者方法。
 *      抽象性 − 抽象性是指将具有一致的数据结构（属性）和行为（操作）的对象抽象成类。一个类就是这样一种抽象，它反映了与应用有关的重要性质，而忽略其他一些无关内容。任何类的划分都是主观的，但必须与具体的应用有关。
 *      封装 − 封装是指将现实世界中存在的某个客体的属性与行为绑定在一起，并放置在一个逻辑单元内。
 *      构造函数 − 主要用来在创建对象时初始化对象， 即为对象成员变量赋初始值，总与new运算符一起使用在创建对象的语句中。
 *      析构函数 − 析构函数(destructor) 与构造函数相反，当对象结束其生命周期时（例如对象所在的函数已调用完毕），系统自动执行析构函数。析构函数往往用来做"清理善后" 的工作（例如在建立对象时用new开辟了一片内存空间，应在退出前在析构函数中用delete释放）。
 *
 */

// 这是一个类的命名空间
namespace ClassSpace {{

    class ClassSite{
        /* 成员变量 */
        var $url;
        var $title;
        var $country;

        /**
         * 访问控制：PHP 对属性或方法的访问控制，是通过在前面添加关键字 public（公有），protetced（受保护）或 private（私有）来实现的
         *      public（公有）：公有的类成员可以在任何地方被访问
         *      protetced（受保护）：受保护的类成员则可以被其自身以及其子类和父类访问
         *      private（私有）：私有的类成员则只能被其定义所在的类访问
         *      注意：类的继承中，可以对 public 和 protetced 进行重定义，但 private 而不能
         *
         *  属性的访问控制：类属性必须定义为公有，受保护，私有之一。如果用 var 定义，则被视为公有。
         *  方法的访问控制：类中的方法可以被定义为公有，私有或受保护。如果没有设置这些关键字，则该方法默认为公有。
         */
        // 属性的访问控制
        public $public = 'Public';
        protetced $protetced = 'Protetced';
        private $private = 'Private';

        function printHello()
        {
            echo $this->public;
            echo $this->protetced;
            echo $this->private;
        }

        /**
         * ClassSite constructor.
         * @param $par1
         * @param $par2
         */
        // 构造函数是一种特殊的方法。主要用来在创建对象时初始化对象， 即为对象成员变量赋初始值，在创建对象的语句中与 new 运算符一起使用
        // 我们就不需要再调用 setTitle 和 setUrl 方法了
//        function __construct($par1, $par2) {
//            $this->url = $par1;
//            $this->title = $par2;
//            echo "这是一个构造函数" . PHP_EOL;
//            $this->name = "ClassSite";
//        }

        function _destruct(){
            echo "销毁 " . $this->name . "\n";
        }

        /* 成员函数 */
        function setUrl($par){
            $this->url = $par;
        }
        function getUrl(){
            echo $this->url . PHP_EOL;
        }
        function setTitle($par){
            $this->title = $par;
        }
        function getTitle(){
            echo $this->title . PHP_EOL;
        }
        function setCountry($par){
            $this->country = $par;
        }
        function getCountry(){
            echo $this->country . PHP_EOL;
        }
    }

    /**
     * Class ChildClass
     *  PHP 使用关键字 extends 来继承一个类，PHP 不支持多继承
     * @package ClassSpace
     */
    class ChildClass extends ClassSite{
        var $category;

        function setCate($par){
            $this->category = $par;
        }
        function getCate($par){
            echo $this->category . PHP_EOL;
        }

        /**
         * 如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写
         */
        function getUrl(){
            echo $this->url . PHP_EOL;
            return $this->url;
        }
        function getTitle(){
            echo $this->title . PHP_EOL;
            return$this->title;
        }
    }

    $mi = new ClassSite("www.mi.com", "mi");


    // 调用成员函数，设置标题和URL
    //    $mi->setUrl("www.mi.com");
    $mi->getUrl();
    $mi->getTitle();


    class Child2Class extends ChildClass {
        // 可以对 public 和 protetced 进行重定义，但 private 而不能
        protetced $protetced = 'Protetced2';

        function printHello(){
            echo $this->public;
            echo $this->protetced;
//            echo $this->private;
        }
    }

    $obj2 = new Child2Class();
    echo $obj2->public;
//    echo $obj2->private; // 未定义 private
//    echo $obj2->protetced; // 这行会产生一个致命错误
    $obj2->printHello(); // 输出 Public、Protetced2 和 Undefined


    /***
     * 接口：使用接口（interface），可以指定某个类必须实现哪些方法，但不需要定义这些方法的具体内容
     *      接口是通过 interface 关键字来定义的，就像定义一个标准的类一样，但其中定义所有的方法都是空的。
     *      接口中定义的所有方法都必须是公有，这是接口的特性
     *      要实现一个接口，使用 implements 操作符。类中必须实现接口中定义的所有方法，否则会报一个致命错误。类可以实现多个接口，用逗号来分隔多个接口的名称
     */
    // 声明一个'iTemplate'接口
    interface iTemplate {
        public function setVariable($name, $var);
        public function getHtml($template);
    }
    // 实现接口
    class Template implements iTemplate{
        private $vars = array();

        public function setVariable($name, $var){
            $this->vars[$name] = $var;
        }

        public function getHtml($template){
            foreach($this->vars as $name => $value) {
                $template = str_replace('{' . $name . '}', $value, $template);
            }
            return $template;
        }
    }

    /**
     * 常量：可以把在类中始终保持不变的值定义为常量。在定义和使用常量的时候不需要使用 $ 符号
     *      常量的值必须是一个定值，不能是变量，类属性，数学运算的结果或函数调用。
     */
    class ConstantClass{
        const constant = '常量值';

        function showConstant() {
            echo  self::constant . PHP_EOL;
        }
    }
    echo PHP_EOL;
    echo ConstantClass::constant . PHP_EOL;


    /**
     * 抽象类：任何一个类，如果它里面至少有一个方法是被声明为抽象的，那么这个类就必须被声明为抽象的
     *        定义为抽象的类不能被实例化
     *        被定义为抽象的方法只是声明了其调用方式（参数），不能定义其具体的功能实现
     *        继承一个抽象类的时候，子类必须定义父类中的所有抽象方法；另外，这些方法的访问控制必须和父类中一样（或者更为宽松）。
     *              例如某个抽象方法被声明为受保护的，那么子类中实现的方法就应该声明为受保护的或者公有的，而不能定义为私有的
     */
    abstract class AbstractClass {
        // 强制要求子类定义这些方法
        abstract protetced function getValue();
        abstract protetced function prefixValue($prefix);

        // 普通方法（非抽象方法）
        public function commonPrint(){
            print $this->getValue() . PHP_EOL;
        }
    }
    class AbstractClass2 extends AbstractClass {
        protetced function getValue()
        {
            // TODO: Implement getValue() method.
            return "AbstractClass";
        }
        public function prefixValue($prefix)
        {
            // TODO: Implement prefixValue() method.
            return "{$prefix}AbstractClass";
        }
    }
    class AbstractClass3 extends AbstractClass {
        protetced function getValue()
        {
            // TODO: Implement getValue() method.
            return "AbstractClass";
        }
        // 子类方法可以包含父类抽象方法中不存在的可选参数 【也就是说：子类定义了一个可选参数，而父类抽象方法的声明里没有，则也是可以正常运行的】
        public function prefixValue($prefix, $separator = ".")
        {
            // TODO: Implement prefixValue() method.
            if ($prefix == "Pacman") {
                $prefix = "Mr";
            } elseif ($prefix == "Pacwoman") {
                $prefix = "Mrs";
            } else {
                $prefix = "";
            }
            return "{$prefix}{$separator} {$prefix}";
        }
    }
    $abstractClass1 = new AbstractClass2();
    $abstractClass1->commonPrint();
    echo $abstractClass1->prefixValue("F00_").PHP_EOL;
    $abstractClass2 = new AbstractClass3();
    echo $abstractClass2->prefixValue("Pacman"), "\n";
    echo $abstractClass2->prefixValue("Pacwoman"), "\n";


    /***
     * 关键词：
     *      Static 关键字
     *          声明类属性或方法为 static(静态)，就可以不实例化类而直接访问。
     *          静态属性不能通过一个类已实例化的对象来访问（但静态方法可以）。
     *          由于静态方法不需要通过对象即可调用，所以伪变量 $this 在静态方法中不可用。
     *          静态属性不可以由对象通过 -> 操作符来访问
     *          可以用一个变量来动态调用类。但该变量的值不能为关键字 self，parent 或 static【PHP 5.3.0 起】
     *      Final 关键字
     *          如果父类中的方法被声明为 final，则子类无法覆盖该方法。如果一个类被声明为 final，则不能被继承
     */
    class StaticClass {
        // 父类的构造方法，这里需要创建的文件为class，不然idea不支持
//        public __construct() {
//            print "BaseClass 类中构造方法" . PHP_EOL;   
//        }

        public static $my_static = 'foo';

        public function staticValue() {
            return self::$my_static;
        }

        final public function moreTesting() {
            echo "BaseClass::moreTesting() called"  . PHP_EOL;
        }
    }
    class StaticClass1 extends StaticClass {
        // 报错信息 Fatal error: Cannot override final method BaseClass::moreTesting()
//        public function moreTesting() {
//           echo "ChildClass::moreTesting() called"  . PHP_EOL;
//        }

        // 调用父类构造方法
//        function __construct() {
//           parent::__construct();  // 子类构造方法不能自动调用父类的构造方法
//           print "SubClass 类中构造方法" . PHP_EOL;
//        }

    }
    class StaticClass2 extends StaticClass {
        // 继承 StaticClass 的构造方法
    }
    print StaticClass::$my_static . PHP_EOL;
    $foo = new StaticClass();
    print $foo->staticValue() . PHP_EOL;
    // 调用父类的构造方法
    $father_obj = new StaticClass();
    // 调用父类、子类的构造方法
    $son_obj = new StaticClass1();
    // 调用父类的构造方法
    $father_obj2 = new StaticClass2();
}
}