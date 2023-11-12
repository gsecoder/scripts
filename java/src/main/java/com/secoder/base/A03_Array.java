package com.secoder.base;

import java.util.Arrays;

/**
 * @file A03_Array
 * @author secoder
 * @date 2020/8/30 8:09 下午
 * @description 数组相关知识
 */

public class A03_Array {
}

class LikeClass {
	public static void main(String[] args) {
		int a[]  = new int[5];
		System.out.println(a[3]);	// a[3]的默认值为0
	}
}

class OneArray {
	public static void main(String[] args) {
		/**
		 * 数组定义在内存的表现形式，我们可以通过debug来获取初始化阶段，各个变量在内存中的表现形式
		 */
		
		// 创建基本类型数组一
		int[] array_1;		// array_1在栈中定义的变量，指向到内存里为空，无任何初始化化值
		/**
		 * 基本数据类型数组在显示赋值之前，Java会自动给他们赋默认值
		 * 默认初始化，array_1指向内存，内存初始化值：array_1=[0, 0, 0, 0. 0]
		 */
		array_1 = new int[5];	// 
		for (int i = 0; i < 5; i++) {
			array_1[i] = i;
			System.out.println("array_1[" + i + "] = " + array_1[i]);
		}
		System.out.println("");
		
		
		// 创建基本类型数组二
		int[] array_2 = new int[5];	// 默认初始化，array_2指向内存，内存初始化值：array_2=[0, 0, 0, 0. 0]
		for (int i = 0; i < 5; i++) {
			array_2[i] = 2 * i;
			System.out.println("array_2[" + i + "] = " + array_2[i]);
		}
	}
}

/**
 * 多维数组（二维）
 */
class MutilArray{
	public static void main(String[] args) {
		/**
		 * 创建方式一：动态初始化1
		 * 	定义了一个二维数组；
		 * 	二维数组中有3个一维数组：array_1[0]、array_1[1]、array_1[2]
		 * 	每一个一维数组中有2个元素；
		 * 	给第一个一维数组1脚标位赋值为77写法是：arr[0][0] = 77;
		 * 	给第一个一维数组2脚标位赋值为78写法是：arr[0][1] = 78;
		 */
		int[][] mutil_array_1 = new int[3][2];
		mutil_array_1[0][0] = 77;
		mutil_array_1[0][1] = 78;
		System.out.println("mutil_array_1: " + Arrays.deepToString(mutil_array_1));
		
		
		/**
		 * 创建方式二：动态初始化2
		 * 	二维数组中有3个一维数组。
		 * 	每个一维数组都是默认初始化值null (注意：区别于格式1）
		 * 	可以对这个三个一维数组分别进行初始化
		 * 
		 */
		int[][] mutil_array_2 = new int[3][];
		mutil_array_2[0] = new int[3]; 
		mutil_array_2[1] = new int[1]; 
		mutil_array_2[2] = new int[2];
		System.out.println("mutil_array_2: " + Arrays.deepToString(mutil_array_2));
		
		/**
		 * 创建方式二：静态初始化
		 * 	定义一个名称为arr的二维数组，二维数组中有三个一维数组
		 * 	每一个一维数组中具体元素也都已初始化
		 * 	第一个一维数组 arr[0] = {0, 1, 2};
		 * 	第二个一维数组 arr[1] = {10,11};
		 * 	第三个一维数组 arr[2] = {20, 21, 22, 23};
		 * 	第三个一维数组的长度表示方式：arr[2].length;
		 * 	
		 * 	注意特殊写法情况：int[]x,y[]; x是一维数组，y是二维数组。
		 * 	Java中多维数组不必都是规则矩阵形式
		 */
		int[][] mutil_array_3 = new int[][]{{0, 1, 2}, {10,11}, {20, 21, 22, 23}};
		System.out.println("mutil_array_3: " + Arrays.deepToString(mutil_array_3));
	}
}