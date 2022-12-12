package base;

/**
 * @file base.A02_Variable
 * @author secoder
 * @date 2022/8/15 16:57
 * @description 变量相关的知识
 */

public class A02_Variable {
	public static void main(String[] args) {
		// main 方法
	}
}

class BaseSyntac {
	// 类变量
	static int a64 = 10;
	// 示例变量，从属于对象的，对象.a65
	int a65 = 65;

	public static void main(String[] args) {
		/*
		 * 八大数据类型
		 * */
		// 整数
		int num1 = 10;
		byte num2 = 20;
		short num3 = 30;
		long num4 = 30L;
		// 浮点数
		float num21 = 0.1f;
		double num22 = 1.0 / 10;
		System.out.print(num21 == num22);
		float n21 = 1232434355f;
		float n22 = n21 + 1;
		System.out.print(n21 == n22);
		double num23 = 3.14159265357589;
		// 字符
		char num31 = '可';
		char n31 = 'a';
		System.out.print((int) num31);
		System.out.print(n31);
		System.out.print((int) n31);
		// 布尔值
		boolean flag = true;
		boolean num42 = false;
		
		
		/*
		 * 强制类型转换
		 * 不能对 布尔值 进行转换
		 * 不能把对象转换为不相干的类型
		 * 在把高容量转换到低容量时，强制转换
		 * 在转换时可能存在内存溢出，或者精度的问题
		 * */
		System.out.print("\n==========强制类型转换============\n");
		System.out.print((int) 23.6 + "\n");
		System.out.print((int) -45.6 + "\n");
		// 强制转换
		char c = 'a';
		int d = c + 1;
		System.out.print(d + "\n");
		System.out.print((char) d + "\n");
		// 内存溢出
		int money = 10_0000_0000;
		int year = 20;
		int salary_1 = money * year;
		System.out.print(salary_1 + "\n");
		long salary_2 = money * (long) year;
		System.out.print(salary_2 + "\n");
		
		
		/*
		 * 变量与常量
		 */
		// 局部变量
		int a61 = 0;
		String a62 = "crisimple";
		char a63 = '7';
		// 获取实例变量
		BaseSyntac var1 = new BaseSyntac();
		System.out.print("实例变量可以通过对象直接使用：" + var1.a65 + "\n");
		// 默认值，声明变量时不给变量赋予默认值
		byte a661 = 0;
		short a662 = 0;
		int a663 = 0;
		float a664 = 0;
		double a665 = 0;
		char a666 = 0;
		boolean a667 = false;
		System.out.print(a661);
		System.out.print(a662);
		System.out.print(a663);
		System.out.print(a664);
		System.out.print(a665);
		System.out.print(a666);
		System.out.print(a667);
		
		
	}
}

/**
 * 进制转换：Decimal conversion
 */
class DecimalConversion {
	public static void main(String[] args) {
		
	}
}

/**
 * 类型转换
 */
class TypeConvert {
	
	/**
	 * 获取变量类型公共方法
	 */
	public static String getType(Object o){
		// 使用int类型的getClass()方法
		return o.getClass().toString();
	}
	
	/**
	 * 类型自动提升
	 */
    static byte byte_variable = 2;
	static int int_variable = 120;
	// byte byte_int_variable = byte_variable + int_variable;  编译不通过
	static int byte_int_variable = byte_variable + int_variable;
	
	static short short_variable = 24;
	//static short byte_short_variable = byte_variable + short_variable; 编译不通过
	static int byte_short_variable = byte_variable + short_variable;
	
	static char char_variable = 56;
	static char char_variable_2 = 57;
	//static char char_variable_3 = char_variable + char_variable_2; 编译不通过
	static int char_variable_3 = char_variable + char_variable_2;
	
	static double double_variable = 12.3;
	static double char_double_variable = char_variable + double_variable;
	
	
	/**
	 * 强制类型转换
	 * @param args
	 */
	static int double_updownto_int_variable = (int)double_variable; // 截断操作
	// 没有损失精度
	static long long_variable = 123;
	static short long_updownto_short_variable = (short)long_variable;
	
	
	public static void main(String[] args){
		System.out.println("byte_int_variable: " + byte_int_variable);
		System.out.println("type of byte_int_variable: " + getType(byte_int_variable));
		
		System.out.println("byte_short_variable: " + byte_short_variable);
		System.out.println("type of byte_short_variable: " + getType(byte_short_variable));
		
		System.out.println("char_variable_3: " + char_variable_3);
		System.out.println("type of char_variable_3: " + getType(char_variable_3));
		
		System.out.println("char_double_variable: " + char_double_variable);
		System.out.println("type of char_double_variable: " + getType(char_double_variable));
		
		System.out.println("double_updownto_int_variable: " + double_updownto_int_variable);
		System.out.println("type of double_updownto_int_variable: " + getType(double_updownto_int_variable));
		
		System.out.println("long_updownto_short_variable: " + long_updownto_short_variable);
		System.out.println("type of long_updownto_short_variable: " + getType(long_updownto_short_variable));
	}
}


/**
 * 引用数据类型：class中的String
 * 	1. String属于引用数据类型，翻译为：字符串
 * 	2. 声明String变量类型时，使用一对""
 * 	3. String可以与8种基本数据类型变量做运算，且运算只能是连接运算：+
 */
class ClassString {
	
	public static void main(String[] args) {
		String s1 = "这是一个字符串";
		System.out.println("s1: " + s1);		// s1: 这是一个字符串
		
		int i1 = 10;
		String si1 = s1 + i1;
		System.out.println("si1: " + si1);		// si1: 这是一个字符串10
		
		boolean b1 = true;
		String sb1 = s1 + b1;					
		System.out.println("sb1: " + sb1);		// sb1: 这是一个字符串true
		
		/**
		 * 任何的数据类型与String类型做连接运算，结果的类型都为String类型
		 */
		char c1 = 'a'; // a:97 A:65
		System.out.println(c1 + i1 + s1);		// 107这是一个字符串
		System.out.println(c1  + s1 + i1);		// a这是一个字符串10
		System.out.println(c1  + (i1 + s1));    // a10这是一个字符串
		System.out.println((c1  + i1) + s1);	// 107这是一个字符串
		System.out.println(s1 + (c1 + i1));		// 这是一个字符串107
	}
}


/**
 * 运算符：operator
 */
class OperatorMark {
	public static void main(String[] args) {
		/*
	 * 算术运算符 +，-，*，/，%，++，--
	 * 赋值运算符 =
	 * 扩展赋值运算符 +=, -=, *=, /=
	 * */
	int a1 = 10;
	int b1 = 20;
	System.out.print(a1 + b1 + "\n");
	System.out.print(a1 - b1 + "\n");
	System.out.print(a1 * b1 + "\n");
	System.out.print((double) a1 / b1 + "\n");
	// 取余运算
	System.out.print(a1 % b1 + "\n");
	// 自增
	System.out.print("=====自增=====\n");
	// a1 = a1 + 1，执行完代码后，先给 b 赋值，a1再自增
	int c11 = a1++;
	System.out.print(a1 + "\n");
	// 执行代码前，a1再自增，先给 b 赋值
	int c12 = ++a1;
	System.out.print(a1 + "\n");
	System.out.print(c11 + "\n");
	System.out.print(c12 + "\n");
	// 自减
	// 扩展赋值运算符
	int a = 10;
	int b = 20;
	a += b;
	b -= a;
	System.out.println("a: " + a);
	System.out.println("b: " + b);
	System.out.print("算术运算符 赋值运算符 扩展赋值运算符 \n\n");
	
	
	/*
	 * 关系运算符：>, <, >=, <=, ==, !=, instanceof
	 * */
	int a21 = 109;
	int a22 = 10;
	byte a13 = '1';
	double a14 = 112.2;
	System.out.print((a21 > a22) + "\n");
	System.out.print((a21 >= a22) + "\n");
	System.out.print((a21 < a22) + "\n");
	System.out.print((a21 < a22) + "\n");
	System.out.print((a21 == a22) + "\n");
	System.out.print((a21 != a22) + "\n");
	System.out.print((a21 != a22) + "\n");
	System.out.print("关系运算符 \n\n");
	
	
	/*
	 * 逻辑运算符：&&, ||, !
	 * */
	boolean a31 = true;
	boolean a32 = false;
	System.out.println("a31&&a32: " + (a31 && a32));
	System.out.println("a31||a32: " + (a31 || a32));
	System.out.println("!(a31 && a32): " + !(a31 && a32));
	System.out.print("逻辑运算符 \n");
	/*
	 * 位运算符：&, |, ^, ~, >>, <<, >>>
	 * a41 = 0011 1100
	 * a42 = 0000 1101
	 *
	 * a41&a42 = 0000 1100
	 * a41|a42 = 0011 1101
	 * a41^a42 = 0011 0001
	 * ~a42 = 1111 0010
	 *
	 * 面试题：2*8 怎样计算最快，左移右移位移效率最高
	 * << *2
	 * >> /2
	 * */
	System.out.println((2 << 3) + "\n");
	
	
	/*
	 * 条件运算符：x？y : z    如果 x 的值为真，则结果为 y；否则结果为 z
	 * */
	int score = 99;
	String type = (score > 60) ? "及格" : "不及格";
	System.out.println(type);
	}
}