package com.secoder.base;

public class MethodDefine {

public static void main(String[] args) {
	int c = add(1, 2);
	System.out.println(c);
}

/**
 * public -- 修饰符
 * int --- 返回值类型
 * add --- 方法名
 * 参数类型 --- int
 * a, b --- 形参
 * 1, 2 --- 实参
 * {return a + b;} --- 方法体
 *
 * @param a, b
 */
public static int add(int a, int b) {
	return a + b;
}
}
