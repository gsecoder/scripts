package com.secoder.base; /**
 * @file com.secoder.base.AnnotationReflectionClassUse
 * @author sf
 * @date 2020/9/1 8:58 下午
 * @description 有了 Class 对象后能做什么？
 */

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class AnnotationReflectionClassUse {

/*
性能分析
 */
// 普通方法调用
public static void commonMethod() {
	TempAnnotationReflectionClassUse tempAnnotationReflectionClassUse11 = new TempAnnotationReflectionClassUse();
	long startTime = System.currentTimeMillis();
	for (int i = 0; i < 1000000000; i++) {
		tempAnnotationReflectionClassUse11.getName();
	}
	long endTime = System.currentTimeMillis();
	System.out.println("普通方式执行10亿次需要耗时：" + (endTime - startTime) + "ms");
}

// 反射方式调用
public static void reflectionMethod() throws ClassNotFoundException, NoSuchMethodException, InvocationTargetException, IllegalAccessException {
	TempAnnotationReflectionClassUse tempAnnotationReflectionClassUse = new TempAnnotationReflectionClassUse();
	Class tempAnnotationReflectionClassUse12 = tempAnnotationReflectionClassUse.getClass();
	Method getName = tempAnnotationReflectionClassUse12.getDeclaredMethod("getName");
	long startTime = System.currentTimeMillis();
	for (int i = 0; i < 1000000000; i++) {
		getName.invoke(tempAnnotationReflectionClassUse, null);
	}
	long endTime = System.currentTimeMillis();
	System.out.println("反射方式执行10亿次需要耗时：" + (endTime - startTime) + "ms");
}

// 反射方式调用，关闭检测
public static void reflectionCloseAccessibleMethod() throws ClassNotFoundException, NoSuchMethodException, InvocationTargetException, IllegalAccessException {
	TempAnnotationReflectionClassUse tempAnnotationReflectionClassUse = new TempAnnotationReflectionClassUse();
	Class tempAnnotationReflectionClassUse13 = tempAnnotationReflectionClassUse.getClass();
	Method getName = tempAnnotationReflectionClassUse13.getDeclaredMethod("getName");
	getName.setAccessible(true);
	long startTime = System.currentTimeMillis();
	for (int i = 0; i < 1000000000; i++) {
		getName.invoke(tempAnnotationReflectionClassUse, null);
	}
	long endTime = System.currentTimeMillis();
	System.out.println("反射方式关闭检测执行10亿次需要耗时：" + (endTime - startTime) + "ms");
}

public static void main(String[] args) throws ClassNotFoundException, NoSuchMethodException, IllegalAccessException, InstantiationException, InvocationTargetException, NoSuchFieldException {
	// main 方法
	commonMethod();
	reflectionMethod();
	reflectionCloseAccessibleMethod();
	
	
	// 获取 Class 对象
	Class c1 = Class.forName("com.java.com.secoder.base.com.secoder.base.TempAnnotationReflectionClassUse");
	
	// 构造一个对象
	TempAnnotationReflectionClassUse tempAnnotationReflectionClassUse1 = (TempAnnotationReflectionClassUse) c1.newInstance();
//		System.out.println("tempAnnotationReflectionClassUse: " + tempAnnotationReflectionClassUse);
	
	// 通过构造器创建对象
	Constructor constructor = c1.getDeclaredConstructor();
	TempAnnotationReflectionClassUse tempAnnotationReflectionClassUse2 = (TempAnnotationReflectionClassUse) constructor.newInstance(10001, "123", 12);
	System.out.println("tempAnnotationReflectionClassUse2: " + tempAnnotationReflectionClassUse2);
	
	// 通过反射调用普通方法
	Method setName = c1.getDeclaredMethod("setName", String.class);
	
	// invoke：激活的意思
	// (对象, "方法的值")
	setName.invoke(c1, "测试者");
	System.out.println(c1.getName());
	
	// 通过反射操作属性
	System.out.println("通过反射操作属性");
	TempAnnotationReflectionClassUse tempAnnotationReflectionClassUse4 = (TempAnnotationReflectionClassUse) c1.newInstance();
	Field name = c1.getDeclaredField("name");
	System.out.println("name: " + name);
	
	// 不能直接操作私有属性， 我们需要关闭程序的安全检测，属性或方法的setAccessible(true)
	name.setAccessible(true);
	name.set(tempAnnotationReflectionClassUse4, "测试者2");
	System.out.println(tempAnnotationReflectionClassUse4.getName());
	
}
}

class TempAnnotationReflectionClassUse {
public int id;
private String name;
private int age;

public TempAnnotationReflectionClassUse() {
	this.id = id;
	this.name = name;
	this.age = age;
}

public int getId() {
	return id;
}

public String getName() {
	return name;
}

public int getAge() {
	return age;
}

public void setId(int id) {
	this.id = id;
}

public void setName(String name) {
	this.name = name;
}

public void setAge(int age) {
	this.age = age;
}

@Override
public String toString() {
	return "com.secoder.base.TempAnnotationReflectionClassUse{" +
			       "id=" + id +
			       ", name='" + name + '\'' +
			       ", age=" + age +
			       '}';
}
}
