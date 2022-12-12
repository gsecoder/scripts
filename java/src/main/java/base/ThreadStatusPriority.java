package base;

/**
 * @file base.ThreadStatusPriority
 * @author sf
 * @date 2020/8/25 8:01 下午
 * @description • 线程优先级：通过线程调度器来监控程序中启动后进入就绪状态的所有线程，线程调度器按优先级决定调度那个线程先执行
 */

public class ThreadStatusPriority {

public static void main(String[] args) {
	// main 方法
	// 主线程为默认优先级
	System.out.println(Thread.currentThread().getName() + "===>>" + Thread.currentThread().getPriority());
	
	// 设置多线程
	MyPriority myPriority = new MyPriority();
	Thread t1 = new Thread(myPriority);
	Thread t2 = new Thread(myPriority);
	Thread t3 = new Thread(myPriority);
	Thread t4 = new Thread(myPriority);
	Thread t5 = new Thread(myPriority);
	Thread t6 = new Thread(myPriority);
	
	// 先设置优先级再启动
	t2.setPriority(Thread.MAX_PRIORITY);
	t3.setPriority(Thread.MIN_PRIORITY);
	t4.setPriority(3);
	t5.setPriority(9);
	t6.setPriority(7);
	
	t6.start();
	t1.start();
	t2.start();
	t3.start();
	t4.start();
	t5.start();
}
}

class MyPriority implements Runnable {
@Override
public void run() {
	System.out.println(Thread.currentThread().getName() + "--->" + Thread.currentThread().getPriority());
}
}
