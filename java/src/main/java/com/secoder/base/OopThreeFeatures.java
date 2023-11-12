package com.secoder.base;

/**
 * @file OOPThreeFeatures
 * @author crisimple
 * @date 2020/8/19 12:16 下午
 * @description 面向对象三大特征
 */

public class OopThreeFeatures {

public static void main(String[] args) {
	// main 方法
	System.out.println("----- 封装 -----");
	Country country = new Country();
	country.setPeople(20_0000_0000);
	country.getPeople();
	
	System.out.println("\n----- 继承 -----");
	China china = new China();
	china.setPeople(14_0000_0000);
	System.out.println(china.getPeople());
	System.out.println("\n.....（1）继承之间属性的调用.....");
	china.printName("这是个printName方法的属性名称");
	System.out.println("\n.....（2）继承之间属性的方法.....");
	china.printMethod();
	System.out.println("\n.....（3）继承中的方法重写.....");
	country.method();
	china.method();
	// 这里通过new 子类来初始化对象，是因为子类继承父类会先super调用父类
	Country co = new China();
	China ch = new China();
	co.method();
	ch.method();
	
	/**
	 * 梳理下类之间的关系
	 * com.secoder.base.China 继承于 com.secoder.base.Country
	 * com.secoder.base.China 有 printS() 方法
	 * com.secoder.base.Country 有 printF() 方法
	 */
	System.out.println("\n----- 多态 -----");
	Country co1 = new China();
	China ch1 = new China();
	System.out.println("\n..... (1) 父类对象转成子类对象 .....");
	// true
	System.out.println("co1 instanceof com.secoder.base.China: " + (co1 instanceof China));
	// true
	System.out.println("ch1 instanceof com.secoder.base.China: " + (ch1 instanceof China));
	// 子类重新父类的方法，因此下面两结果均为：com.secoder.base.China.method()
	co1.method();
	ch1.method();
	System.out.println("\n..... (2) 父类对象转成子类对象（强制转换） .....");
	// 如果想要让父类获取到子类的特有方法printS()，要将父类对象co1强制转换为子类的类型（高-->低），所以要进行强制类型转换
	// printF() 为父类的方法，父类对象 co1 可以直接访问结果为：County Method；强制转换后父类对象可以访问到子类独有方法，结果为：com.secoder.base.China Method
	co1.printF();
	((China) co1).printS();
	System.out.println("\n..... (3) 子类对象转换为父类对象（自动转换） .....");
	China ch2 = new China();
	// 子类对象 ch2 可以直接访问到父类的特有方法 printF()，输出结果为：County Method，因为是继承父类的，所以可以获取到父类的一切！
	ch2.printF();
	// 将子类对象强制转换为父类的类型，可能会丢失子类自己本身的一些方法!!!
	Country ch3 = ch2;
	ch2.printF();
	ch2.printS();
//        ch3.printS();
	
}
}

/**
 * 子类继承父类
 */
class China extends Country {

private String name = "China的自带属性名称";

/**
 * 子类的无参构造器
 */
public China() {
//       super();   隐藏的代码，也可以显示写，调用了父类的无参构造器
	String name = "中国";
}

/**
 * 子类的有参构造器
 *
 * @param name
 */
public China(String name) {
	System.out.println("com.secoder.base.China 的有参构造器" + name);
}

public void printName(String name) {
	System.out.println(name);
	System.out.println(this.name);
	System.out.println(super.getName());
}

public void printMethod() {
	printS();
	this.printS();
	super.printF();
}

public void printS() {
	System.out.println("com.secoder.base.China Method");
}

@Override
public void method() {
	System.out.println("com.secoder.base.China.method()");
}
}

/**
 * 封装实例
 */
class Country extends Object {
/**
 * 类的私有属性
 */
private String name = "我是父类的自导属性名称";
private float area;
private double people;

/**
 * 统一提供一些可以操作这个属性的方法，set/get方法
 *
 * @return
 */
public String getName() {
	return name;
}

public void setName(String name) {
	this.name = name;
}

public float getArea() {
	return area;
}

public void setArea(float area) {
	this.area = area;
}

public double getPeople() {
	return people;
}

public void setPeople(double people) {
	if(people > 10_0000_0000) {
		this.people = people;
		System.out.println("超大国家");
	} else {
		System.out.println("小国家");
	}
}

public void printF() {
	System.out.println("County Method");
}

public void method() {
	System.out.println("com.secoder.base.Country.method()");
}
	
}
