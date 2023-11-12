package com.secoder.base;

/**
 * @file com.secoder.base.MethodReload
 * @author crisimple
 * @date 2020/8/13 10:59 上午
 * @description
 */

public class MethodReload {

public static double add(double a, double b) {
	return a + b;
}

public static int add(int a, int b) {
	return a + b;
}

public static double add(int a, int b, int c) {
	return a + b;
}

public static void main(String[] args) {
	System.out.println(add(11, 23));
	
	System.out.println(add(11.2, 23.1));
	
	System.out.println(add(1, 2, 3));
	
}
}
