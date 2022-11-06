/**
 * @file ThreadSynUnsafeBuyTicket
 * @author sf
 * @date 2020/8/26 7:04 下午
 * @description 线程同步不安全的买票
 * --->>
 * 通过线程同步解决该问题
 */

public class ThreadSyncUnsafeBuyTicket {

public static void main(String[] args) {
	// main 方法
	
	BuyTicket buyTicket = new BuyTicket();
	
	// 创建多线程
	new Thread(buyTicket, "旅客").start();
	new Thread(buyTicket, "黄牛").start();
	new Thread(buyTicket, "学生").start();
	
}
}


/**
 * 不安全的买票
 */
class BuyTicket implements Runnable {
// 总票数
private int ticketNums = 10;
// 外部停止方法
boolean flag = true;

// 定义不停止买票的函数
@Override
public void run() {
	while (flag) {
		buy();
	}
}


public synchronized void buy() {
	if(ticketNums <= 0) {
		flag = false;
		return;
	}
	
	// 增加延时，方法抢占问题
	try {
		Thread.sleep(1000);
	} catch (InterruptedException e) {
		e.printStackTrace();
	}
	
	System.out.println(Thread.currentThread().getName() + " ---> 买到了第 " + ticketNums-- + "票。");
}
}
