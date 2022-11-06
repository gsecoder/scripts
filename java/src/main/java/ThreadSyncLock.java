/**
 * @file ThreadSyncLock
 * @author sf
 * @date 2020/8/27 1:04 上午
 * @description Lock 锁
 */

import java.util.concurrent.locks.ReentrantLock;

public class ThreadSyncLock {

public static void main(String[] args) {
	// main 方法
	LockBuyTicket lockBuyTicket = new LockBuyTicket();
	
	new Thread(lockBuyTicket, "a1").start();
	new Thread(lockBuyTicket, "a2").start();
	new Thread(lockBuyTicket, "a3").start();
}
}

class LockBuyTicket implements Runnable {
int ticketNums = 10;

// 定义可重入锁
private final ReentrantLock lock = new ReentrantLock();

@Override
public void run() {
	while (true) {
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		try {
			// 加锁
			lock.lock();
			
			if(ticketNums > 0) {
//					try {
//						Thread.sleep(1000);
//					} catch (InterruptedException e) {
//						e.printStackTrace();
//					}
				System.out.println(Thread.currentThread().getName() + " 拿到第 " + ticketNums-- + " 票");
			} else {
				return;
			}
		} finally {
			lock.unlock();
		}
	}
	
}
}