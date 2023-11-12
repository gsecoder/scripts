package com.secoder.base;

public class ProcessLoopSample {
public static void main(String[] args) {
	// 计算 0-100 之间的奇数和偶数的和
	int oddSum = 0;
	int evenSum = 0;
	
	for (int i = 0; i <= 100; i++) {
		if(i % 2 == 0) {
			evenSum += i;
		} else {
			oddSum += i;
		}
	}
	System.out.println("奇数之和oddSum: " + oddSum);
	System.out.println("奇数之和evenSum: " + evenSum);
	System.out.println("\n===== end =====");
	
	
	// 输出 1-1000 之间能被5整除的数，并且每行输出3个
	for (int i = 0; i <= 1000; i++) {
		if(i % 5 == 0) {
			System.out.print(i + "\t");
		}
		if(i % (5 * 3) == 0) {
			System.out.println();
		}
	}
	System.out.println("\n===== end =====");
	
	
	// 打印就九九乘法表
	for (int i = 1; i <= 9; i++) {
//            System.out.println(1+"*"+i+"="+(1*i));
		for (int j = 1; j <= i; j++) {
			System.out.print(j + "*" + i + "=" + (i * j) + "\t");
		}
		System.out.println();
	}
	System.out.println("===== end =====");
	
	
	// 打印 5 行的三角形
	for (int i = 1; i <= 5; i++) {
		for (int j = 5; j >= i; j--) {
			System.out.print(" ");
		}
		for (int j = 1; j <= i; j++) {
			System.out.print("*");
		}
		for (int j = 1; j < i; j++) {
			System.out.print("*");
		}
		System.out.println();
	}
	
}
}
