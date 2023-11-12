package com.secoder.base; /**
 * @file com.secoder.base.ArrayUse
 * @author sf
 * @date 2020/8/16 8:09 下午
 * @description 数组的使用
 */

public class ArrayUse {

public static void main(String[] args) {
//        Arrays
	
	int[] arrays = {1, 2, 3, 4, 5, 6};
	System.out.println("for...each");
	foreach(arrays);
	
	System.out.println("数组作为方法入参int");
	printArray(arrays);
	
	System.out.println("数组作为返回值");
	int[] reverseResult = reverseArray(arrays);
	printArray(reverseResult);
	
	System.out.println("多维数组...");
	int[][] mulitArrays = {{1, 2, 3}, {2, 3, 4}, {3, 4, 5}, {4, 5, 6}, {5, 6, 7}};
	printMulitArray(mulitArrays);
}

/**
 * for...each
 */
public static void foreach(int[] args) {
	for (int arg : args) {
		System.out.println(arg);
	}
}

/**
 * 数组作为方法入参int
 *
 * @param arrays
 */
public static void printArray(int[] arrays) {
	for (int i = 0; i < arrays.length; i++) {
		System.out.println(arrays[i]);
	}
}

/**
 * 数组作为返回值
 *
 * @param args
 * @return
 */
public static int[] reverseArray(int[] args) {
	int[] result = new int[args.length];
	for (int i = 0, j = args.length - 1; i < args.length; i++, j--) {
		result[j] = args[i];
	}
	return result;
}

/**
 * 多维数组
 *
 * @param args
 */
public static void printMulitArray(int[][] args) {
//        int[][] arrays = new int[3][5];
	int[][] arrays = args;
	for (int i = 0; i < arrays.length; i++) {
		for (int j = 0; j < arrays[i].length; j++) {
			System.out.println(arrays[i][j]);
//                System.out.println(arrays[i]);
		}
	}
}
	
	
}
