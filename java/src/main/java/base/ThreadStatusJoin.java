package base;/*
 * @file base.ThreadStatusJoin
 * @author sf
 * @date 2020/8/25 7:12 下午
 * @description 插队线程
 */

public class ThreadStatusJoin implements Runnable {

public static void main(String[] args) {
	// main 方法
	// 启动vip线程
	ThreadStatusJoin threadStatusJoin = new ThreadStatusJoin();
	Thread thread = new Thread(threadStatusJoin);
	thread.start();
	
	// 主线程
	for (int i = 0; i < 500; i++) {
		if(i == 200) {
			try {
				thread.join();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		System.out.println("main主线程--->" + i);
	}
}

@Override
public void run() {
	for (int i = 0; i < 500; i++) {
		System.out.println("子线程VIP===>>" + i);
	}
}
}

class TempThreadStatusJoin {
// 空类
}
