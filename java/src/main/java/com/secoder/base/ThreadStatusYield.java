package com.secoder.base;

/**
 * @file ThreadStatusYeild
 * @author sf
 * @date 2020/8/25 6:55 下午
 * @description yield 线程礼让：让当前正在执行的线程暂停，但不阻塞；当线程从运行状态转为就绪状态。CPU 的重新调度不一定礼让成功，看CPU心情
 */

public class ThreadStatusYield {

public static void main(String[] args) {
	// main 方法
	
	MyYield myYield = new MyYield();
	new Thread(myYield, "a").start();
	new Thread(myYield, "b").start();
}
}


class MyYield implements Runnable {
@Override
public void run() {
	System.out.println(Thread.currentThread().getName() + "线程开始执行");
	Thread.yield();
	System.out.println(Thread.currentThread().getName() + "线程停止执行");
}
}
