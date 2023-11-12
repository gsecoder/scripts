package com.secoder.base; /**
 * @file com.secoder.base.ArraySort
 * @author sf
 * @date 2020/8/17 9:49 下午
 * @description 八大排序方法
 */

import java.util.Arrays;

public class ArraySort {

public static void main(String[] args) {
	// main 方法
	int[] arrays = {1, 7, 5, 3, 2, 9};
	
	// 冒泡排序
	int[] sort_arrays = bubble(arrays);
	System.out.println("冒泡排序结果为：" + Arrays.toString(sort_arrays));
	;
	
}

/**
 * 冒泡排序：
 *
 * @param args
 */
public static int[] bubble(int[] args) {
	// 临时变量
	int temp = 0;
	// 定义标志位减少没有意义的比较
	boolean flag = false;
	
	// 外层循环，判断当前数组要比较多少次
	for (int i = 0; i < args.length - 1; i++) {
		// 内层循环比较元素大小，如果第一个数比第二个数大，则交换位置
		for (int j = 0; j < args.length - 1 - i; j++) {
			if(args[j + 1] < args[j]) {
				temp = args[j];
				args[j] = args[j + 1];
				args[j + 1] = temp;
				flag = true;
			}
		}
		if(flag = false) {
			break;
		}
	}
	return args;
}
}
