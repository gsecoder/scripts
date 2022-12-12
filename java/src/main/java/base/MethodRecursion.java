package base;

/**
 * @file base.MethodRecursion
 * @author sf
 * @date 2020/8/13 9:45 下午
 * @description 递归
 * @example: f(5) = 5 * 4 * 3 * 2 * 1
 */

public class MethodRecursion {

public static void main(String[] args) {
	// main 方法
	System.out.println(factorial(1));
	System.out.println(factorial(5));
}

public static int factorial(int n) {
	// 递归头：什么时候不调用自身方法。如果没有头，将陷入死循环
	if(n == 1) {
		return 1;
	} else {
		// 递归体：什么时候需要调用自身方法
		return n * factorial(n - 1);
	}
}
}
