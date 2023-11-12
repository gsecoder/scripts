package com.secoder.base;

/**
 * @file com.secoder.base.AnnotationReflectionClass
 * @author sf
 * @date 2020/8/31 8:36 下午
 * @description Class 类的
 */

public class AnnotationReflectionClass {

public static void main(String[] args) {
	// main 方法
	
	PersonClass personClass = new StudentClass();
	System.out.println("这个人是：" + personClass.name);
	
	// 1、通过对象获取
	Class c1 = personClass.getClass();
	System.out.println(c1.hashCode());
	
	// 2、forName 获取
	try {
		Class c2 = Class.forName("com.java.com.secoder.base.com.secoder.base.StudentClass");
		System.out.println(c2.hashCode());
	} catch (ClassNotFoundException e) {
		e.printStackTrace();
	}
	
	// 3、通过 类名.class 获得
	Class c3 = StudentClass.class;
	System.out.println(c3.hashCode());
	
	// 4、基本类型的包装类都有一个 Type 属性
	Class<Integer> type = Integer.TYPE;
	System.out.println(type);
	
	// 5、获得父类型
	Class c5 = c1.getSuperclass();
	System.out.println(c5);
}
}

/**
 * 父类：Person 类
 */
class PersonClass {
public String name;

public PersonClass() {
}

public PersonClass(String name) {
	this.name = name;
}
}

/**
 * 子类：com.secoder.base.TeacherClass 类
 */
class TeacherClass extends PersonClass {
public TeacherClass() {
	this.name = "老师";
}
}

/**
 * 子类：com.secoder.base.StudentClass 类
 */
class StudentClass extends PersonClass {
public StudentClass() {
	this.name = "学生";
}
}