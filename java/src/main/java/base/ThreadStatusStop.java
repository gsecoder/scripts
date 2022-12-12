package base;/*
 * @file ThreadStatus
 * @author sf
 * @date 2020/8/24 9:01 下午
 * @description 线程状态
 * • 停止线程：不推荐使用JDK的stop() 、destory()方法；建议使用标志位进行终止变量，当 flag=false，则线程终止
 */

public class ThreadStatusStop implements Runnable {

// 1. 设置一个标志位
private boolean flag = true;

@Override
public void run() {
	int i = 0;
	// 3. 线程体中使用该标志位
	while (flag) {
		System.out.println("run...Thread " + i++);
	}
}

/**
 * 2. 设置一个公开的方法停止线程，转换标准位
 */
public void stop() {
	this.flag = false;
}

public static void main(String[] args) {
	// main 方法
	ThreadStatusStop threadStatusStop = new ThreadStatusStop();
	new Thread(threadStatusStop).start();
	
	// 创建主线程在主线程中去切换线程
	for (int i = 0; i < 1000; i++) {
		System.out.println("main方法主线程：" + Thread.currentThread().getName() + "--->" + i);
		if(i == 800) {
			// 调用 stop() 方法切换标志位，让线程停止
			threadStatusStop.stop();
			System.out.println("线程该停止了...");
		}
	}
}
}

class TempThreadStatusStop {
// 空类
}
