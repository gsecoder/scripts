package com.secoder.base;

/**
 * @file OopMuiltClass
 * @author sf
 * @date 2020/8/21 8:31 下午
 * @description 各种骚操作类
 */

public class OopVariousClass {

public static void main(String[] args) {
	// main 方法
	
	/**
	 * 匿名内部类
	 */
	System.out.println(new OopVariousClass().toString());
}
	
	
}

/**
 * 外部类
 */
class Outer {
private String name = "OUTER";

public void out() {
	System.out.println("外部类的方法...");
}

public void outPartMethod() {
	/**
	 * 局部内部类
	 */
	class Inner1Part {
		public void inner1Method() {
			System.out.println("局部内部类的方法");
		}
	}
}

/**
 * 内部类
 */
public class Inner {
	public void in() {
		System.out.println("内部类的方法...");
	}
	
	public void inGetOut() {
		System.out.println(name);
	}
}
}