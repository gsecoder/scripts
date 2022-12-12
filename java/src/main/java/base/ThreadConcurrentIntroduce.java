package base;

/**
 * @file base.ThreadConcurrentIntroduce
 * @author sf
 * @date 2020/8/24 1:40 下午
 * @description 线程并发初认识，并发未控制会出现对同一个资源进行抢占的问题
 * 模拟人们抢火车票场景
 * 旅客--->抢到了第 10 票
 * 黄牛--->抢到了第 9 票
 * 旅游网站--->抢到了第 8 票
 * 旅客--->抢到了第 7 票
 * 黄牛--->抢到了第 6 票
 * 旅游网站--->抢到了第 5 票
 * 旅客--->抢到了第 4 票
 * 黄牛--->抢到了第 4 票
 * 旅游网站--->抢到了第 3 票
 * 旅客--->抢到了第 2 票
 * 黄牛--->抢到了第 1 票
 * 旅游网站--->抢到了第 0 票
 * 旅客--->抢到了第 -1 票
 * 黄牛--->抢到了第 -2 票
 * <p>
 * 通过输出接口可以看到不同的线程会对同一个资源进行抢占，所以得对线程进行管控处理
 */

public class ThreadConcurrentIntroduce implements Runnable {

// 总票数
private int ticketNum = 10;

public static void main(String[] args) {
	// main 方法
	ThreadConcurrentIntroduce threadConcurrentIntroduce = new ThreadConcurrentIntroduce();
	
	new Thread(threadConcurrentIntroduce, "旅客").start();
	new Thread(threadConcurrentIntroduce, "黄牛").start();
	new Thread(threadConcurrentIntroduce, "旅游网站").start();
}

@Override
public void run() {
	while (true) {
		if(ticketNum < 0) {
			break;
		}
		// 模拟延时
		try {
			Thread.sleep(200);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		System.out.println(Thread.currentThread().getName() + "--->抢到了第 " + ticketNum-- + " 票");
	}
}
}

class BuyTickets {
// 没代码了
}
