package base; /**
 * @file base.ThreadPool
 * @author sf
 * @date 2020/8/27 2:16 上午
 * @description
 */

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ThreadPool {

public static void main(String[] args) {
	MyPool myPool = new MyPool();
	
	// 1.创建线程池服务
	ExecutorService executorService = Executors.newFixedThreadPool(3);
	
	// 2.执行
	executorService.execute(myPool);
	executorService.execute(myPool);
	executorService.execute(myPool);
	executorService.execute(myPool);
	
	// 3.关闭服务
	executorService.shutdown();
	
}
}

class MyPool implements Runnable {
@Override
public void run() {
	System.out.println(Thread.currentThread().getName());
}
}
