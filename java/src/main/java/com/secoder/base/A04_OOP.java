package com.secoder.base; /**
 * @file A04_OOP
 * @author secoder
 * @date 2020/8/30 8:09 下午
 * @description 数组相关知识
 */


import java.util.Date;

import static java.lang.Math.PI;

/**
 * 类的创建与使用
 */
class ClassObject {
    
    /**
     * 属性或成员变量
     */
    public String name;
    public int age;
    public boolean isMarried;
    
    /**
     * 构造器
     */
    public ClassObject(){}
    public ClassObject(String n, boolean im){
        name = n;
        isMarried = im;
    }
	
	public String display() {
        return "名字是：" + name + "年龄是：" + age + "是否结婚：" + isMarried;
    }
	
    /**
     * 代码块
     */
	{
		name = "你的名字";
		age = 17;
		isMarried = true;
	}
	
	/**
	 * 内部类
	 */
	class Pet{
		String name;
		float weight;
	}
	
}

/**
 * 内存分析
 */
class MemoryAnalysis {
	String name = "A";
	int num = 1;
	
	void show() {
		System.out.println("name = " + name + " ;num = " + num);
	}
}
class MemoryAnalysisTest {
	public static void main(String[] args) {
		MemoryAnalysis ma1 = new MemoryAnalysis();	// 建立对象1
		MemoryAnalysis ma2 = new MemoryAnalysis();	// 建立对象2
		MemoryAnalysis ma3 = ma2;
		ma2.name = "B";		// 对对象的属性进行修改
		ma1.show();			// 使用对象的方法
		ma2.show();
		ma3.show();
	}
}

/**
 * 类的三大特性：封装
 */
class ClassThreeFeaturePackage{
	public int legs;	// 将属性legs定义为private，只能被ClassThreeFeaturePackage类内部访问
	public void setLegs(int i){
		if (i != 0 && i != 2 && i != 4){
			System.out.printf("Wrong numbers of legs~");
			return;
		}
		legs = i;
	}
	public int getLegs() {
		return legs;
	}
}

/**
 * 类的三大特性：继承
 */
class ClassThreeFeatureInheritanceFather{
	public String name;
	public int age;
	public Date birthDate;

	@Override
	public String toString() {
		return "ClassThreeFeatureInheritanceFather{" +
				"name='" + name + '\'' +
				", age=" + age +
				", birthDate=" + birthDate +
				'}';
	}

	public String getInfo(){
		return "Name: " + name + "\n age: " + age;
	}
}
class ClassThreeFeatureInheritanceSon extends ClassThreeFeatureInheritanceFather{
	/**
	 * 类继承了父类Father的所有属性和方法，并增加了一个属性school。
	 * Father中的属性和方法, Son都可以使用
	 */
	protected String name = "我是子类";
	protected String school = "子类学校";


	public ClassThreeFeatureInheritanceSon(int i, String s, String dd, String qq) {
		super();
	}

	/**
	 * 子类对父类方法的重写
	 * 	子类不能对父类定义为private的方法重写
	 * 	子类不能对父类定义为static的方法重写，static定义的方法只属于父类
	 * 	除上面两条之外，子类能对父类同名、同参数的方法进行重写
	 * @return
	 */
	@Override
	public String toString() {
		return "ClassThreeFeatureInheritanceSon{" +
				"school='" + school + '\'' +
				", name='" + name + '\'' +
				", age=" + age +
				", birthDate=" + birthDate +
				'}';
	}

	/**
	 * 重写父类的方法
	 */
	public String getInfo(){
		return super.getInfo() + "\n name: " + this.name + "\n school: " + this.school;
	}
}
class ClassThreeFeatureTest{
	public static void main(String[] args) {
		// 类的三大特性：封装
		ClassThreeFeaturePackage ctfp = new ClassThreeFeaturePackage();
		ctfp.setLegs(100);
		System.out.printf("100: " + String.valueOf(ctfp.getLegs()));
		System.out.printf("\n");
		ctfp.setLegs(2);
		System.out.printf("2: " + String.valueOf(ctfp.getLegs()));
		System.out.printf("\n");


		// 类的三大特性：继承
		ClassThreeFeatureInheritanceSon ctfis = new ClassThreeFeatureInheritanceSon(
			1,"12", "dd", "qq"
		);
		System.out.printf("查看子类的继承输出：" + ctfis.getInfo());
	}
}

/**
 * 类的三大特征：多态
 */
class ClassThreePolymorphic{

}




/**
 * 深入了解方法：值传递
 */
class MethodParameterTransferPerson{
    int age;
	
	public int getAge() {
		return age;
	}
	
	public void setAge(int age) {
		this.age = age;
	}
}
class MethodParameterTransfer{
	
	MethodParameterTransferPerson mptp = new MethodParameterTransferPerson();
	
	int x;
	int age;
	//MethodParameterTransferPerson mptp = new MethodParameterTransferPerson();
	
    // 基本数据类型的参数传递
    public int setX(int x) {
        System.out.println("【基本数据类型的参数传递】change之前的x=" + x);
        x = 2;
        System.out.println("【基本数据类型的参数传递】change之后的x=" + x);
		return x;
    }
	public int getX() {
		return x;
	}

    // 引用数据类型的参数传递
    public void setAge(MethodParameterTransferPerson obj){
        System.out.println("【引用数据类型的参数传递】change之前的age=" + obj.age);
        obj.age = 22;
        System.out.println("【引用数据类型的参数传递】change之后的age=" + obj.age);
    }
	public int getAge(MethodParameterTransferPerson obj) {
		return obj.age;
	}
}
class MethodParameterTransferTest{
	public static void main(String[] args) {
		MethodParameterTransfer mpt = new MethodParameterTransfer();
		
		// 基本数据类型的参数传递
		mpt.setX(20);
		mpt.getX();
		
		// 引用数据类型的参数传递
		MethodParameterTransferPerson mptp = new MethodParameterTransferPerson();
		mptp.age = 2;
		mpt.setAge(mptp);
		mpt.getAge(mptp);
	}
}

/**
 * 深入了解方法：递归方法
 */
class MethodRepeat{
	// 计算1~100之间所有自然数的和
	public static int sum(int num){
		if(num==1){
			return 1;
		}else{
			return num + sum(num-1);
		}
	}
	
	public static void main(String[] args) {
		System.out.println("1~100之间所有自然数的和为：" + MethodRepeat.sum(100));;
	}
}


/**
 * 关键字keyword：this
 */
class KeywordThis{
	private String name;
	private int age;

	/**
	 * 【无参构造器】
	 */
	public KeywordThis(){
		System.out.println("新对象实例化，" + this.getClass() + "本类的无参构造器~" + "\n") ;
	}

	/**
	 * 【有参构造器】
	 */
	public KeywordThis(String name){
		// 调用本类中的无参构造器
		this();

		this.name = name;
	}

	/**
	 * 【有参构造器】
	 * 在任意方法或构造器内，如果使用当前类的成员变量或成员方法可以在其前面添加this，增强程序的阅读性。
	 * 不过，通常我们都习惯省略this。
	 * 当形参与成员变量同名时，如果在方法内或构造器内需要使用成员变量，必须添加this来表明该变量是类的成员变量
	 */
	public KeywordThis(String name, int age){
		// 调用本类中的有参构造器;【this可以作为一个类中构造器相互调用的特殊格式】
		this(name);

		this.age = age;
	}

	public void getInfo(){
		System.out.printf("说出你的姓名：" + name + "\n");

		// 使用this访问属性和方法时，如果在本类中未找到，会从父类中查找
		this.speak();
	}

	public void speak(){
		System.out.printf("说出你的年龄为：" + age);
	}

	public static void main(String[] args) {
		KeywordThis kt = new KeywordThis("你的名字", 12);
		kt.getInfo();
	}
}

/**
 * 关键字keyword：static
 */
class KeywordStatic{
	/**
	 * 静态属性，随类一起加载
	 */
	public static String name;
	/**
	 * 非静态属性
	 */
	public int age;

	/*
	匿名代码块
	 */ {
		System.out.println("这是匿名代码块");
	}

	/*
	静态代码块，最早执行，且只执行一次
	 */
	static {
		System.out.println("这是静态代码块");
	}

	/*
	构造方法
	 */
	public KeywordStatic() {
		System.out.println("这是无参构造器");
	}

	/**
	 * 静态方法，随类一起加载
	 */
	public static void staticMethod() {
		System.out.println("static method");
	}

	/**
	 * 非静态方法，需要实例化对象，对象来调用
	 */
	public void noStaticMethod() {
		/**
		 * 因为静态方法跟随类一起加载，所以在非静态方法中可以直接调用，反之则不能
		 */
		staticMethod();
		System.out.println("no static method");
	}
}
class KeywordStaticTest{
	public static void main(String[] args) {
		// main 方法
		/**
		 * 静态方法，类是直接可以调用的，因为他们是随类一起加载的
		 */
		KeywordStatic.staticMethod();
		System.out.println(KeywordStatic.name);

		/**
		 * 非静态的
		 */
		KeywordStatic ks = new KeywordStatic();
		ks.noStaticMethod();
		System.out.println(ks.age);

		/**
		 * 看下静态代码块、匿名代码块和构造器的执行顺序
		 */
		KeywordStatic ks2 = new KeywordStatic();

		/**
		 * 静态导入包，第一个为非静态导入包之前的调用，第二个为静态导入包后的调用
		 */
		//        System.out.println(Math.PI);
		System.out.println(PI);
	}
}
class KeywordStaticSingletonHunger{
	// 饿汉模式
	// 1. 私有化构造器
	private KeywordStaticSingletonHunger(){

	}

	// 2. 内部提供一个当前类的实例化
	// 4. 此实例（对象）也必须静态化
	private static KeywordStaticSingletonHunger kssh = new KeywordStaticSingletonHunger();

	// 3. 提供公共的静态方法，返回当前类的对象
	public static KeywordStaticSingletonHunger getInstance(){
		return kssh;
	}
}
class KeywordStaticSingleLazy{
	// 懒汉模式
	// 1. 私有化构造器
	private KeywordStaticSingleLazy(){

	}

	// 2. 内部提供一个当前类的实例化
	// 4. 此实例也必须静态化
	private static KeywordStaticSingleLazy kssl;

	// 3. 提供公共的静态方法，返回当前类的对象
	public static KeywordStaticSingleLazy getInstance(){
		if (kssl==null){
			kssl = new KeywordStaticSingleLazy();
		}
		return kssl;
	}
}


public class A04_OOP {
	public static void main(String[] args) {
		ClassObject co = new ClassObject();
		System.out.println(co.name);	// 访问属性
	}
}