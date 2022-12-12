package base;

/**
 * @file OOPCreate
 * @author sf
 * @date 2020/8/18 9:05 下午
 * @description
 */

public class OopCreate {

public static void main(String[] args) {
	// main 方法
	Company company = new Company();
	System.out.println(company.name);
	company.name = "小米";
	System.out.println(company.name);
}
	
	
}

class Company {
String name;
int age;

/**
 * 无参构造器（一般情况都是隐式定义，在有有参构造器的时候无参构造器必须显示定义）
 */
public Company() {
	
}

/**
 * 有参构造器
 *
 * @param name
 * @param age
 */
public Company(String name, int age) {
	/**
	 * this 代指 base.Company 类
	 * this.name 中的 name 指的是 base.Company 的属性
	 * = name 中的 name 指的是有参构造器中的参数 name
	 */
	this.name = name;
	this.age = age;
}
	
}
