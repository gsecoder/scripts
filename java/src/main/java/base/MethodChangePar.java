package base; /**
 * @file base.MethodChangePar
 * @author sf
 * @date 2020/8/13 9:22 下午
 * @description 可变参数
 */

import java.util.Arrays;

public class MethodChangePar {

public static void main(String[] args) {
	MethodChangePar mcp = new MethodChangePar();
	
	// 多参数
	mcp.test(12.2, 1, 5);
	
	// 输出最大值
	printMax(12.7, 12.0, 21, 23.9, 13.7, 129, 99.1);
}

public void test(double a, int... i) {
	System.out.println("a: " + a);
	System.out.println("i: " + i[0]);
	System.out.println("i: " + Arrays.toString(i));
}

public static void printMax(double... numbers) {
	if(numbers.length == 0) {
		System.out.println("No Arguments Input");
		return;
	}
	
	double result = numbers[0];
	
	// 排序
	for (double number : numbers) {
		if(number > result) {
			result = number;
		}
	}
	System.out.println("The Max Number is: " + result);
}
}
