package com.secoder.base;

/**
 * @file com.secoder.base.OopException
 * @author sf
 * @date 2020/8/21 9:48 下午
 * @description Exception 异常处理
 */

public class OopException {

public static void main(String[] args) {
	// main 方法
	
	int a = 1;
	int b = 0;
	
	try {
		/**
		 * try 监控区
		 * catch(ArithmeticException-想要航获的异常类型)异常捕获，从小到大依次捕获
		 */
		System.out.println(a / b);
		
		/**
		 * 自定义异常类的测试调用
		 */
		new OopException().testa(10);
		new OopException().testa(12);
	} catch (ArithmeticException e) {
		System.out.println("除0异常被捕获");
		// 打印错误信息
		e.printStackTrace();
	} catch (Error er) {
		System.out.println("Error错误");
	} catch (Exception ex) {
		System.out.println("Exception异常");
	} catch (Throwable th) {
		System.out.println("Throwable");
	} finally {
		/**
		 * 非必须项
		 * 处理程序完后的事（IO资源关闭、数据库连接关闭等），不管是否异常都执行
		 */
		System.out.println("finally");
	}
	
	/**
	 * 自定义异常类
	 */
	
	
}

/**
 * 主动抛出异常
 */
public void test(int a, int b) throws ArithmeticException {
	if(b == 0) {
		// 主动的抛出异常，一般在方法中使用
		throw new ArithmeticException();
	}
	System.out.println(a / b);
}

public void testa(int a) throws MyException {
	System.out.println("details = " + a);
	if(a > 10) {
		throw new MyException(a);
	}
	System.out.println("a小于10，OK！");
}

public void a() {
	b();
}

public void b() {
	a();
}
}

class MyException extends Exception {
private int detail;

/**
 * 用构造器定义输出信息
 */
public MyException(int a) {
	// this 指代 com.secoder.base.MyException 类
	this.detail = a;
}

@Override
public String toString() {
	return "com.secoder.base.MyException{" + "detail=" + detail + '}';
}
}
