/**
 * @file ThreadRealization
 * @author sf
 * @date 2020/8/23 10:34 上午
 * @description 线程实现（重点）
 */

public class ThreadRealizationExtendsThread extends Thread {

@Override
public void run() {
	// run 方法线程体
	for (int i = 0; i < 20; i++) {
		System.out.println("子线程：我在写代码----" + i);
	}
}

public static void main(String[] args) {
	// main 方法
	// main 线程，主线程
	// 创建线程对象
	ThreadRealizationExtendsThread threadRealizationExtendsThread = new ThreadRealizationExtendsThread();
	// 主线程调用 start() 方法，同时开启子线程
	threadRealizationExtendsThread.start();
	
	// 调用子线程方法
	threadRealizationExtendsThread.run();
	for (int i = 0; i < 1_000; i++) {
		System.out.println("主线程：我在学习多线程----" + i);
	}
}
}

class TempClass {
	
}