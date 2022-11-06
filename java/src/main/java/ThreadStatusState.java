/**
 * @file ThreadStatusState
 * @author sf
 * @date 2020/8/25 7:36 下午
 * @description 线程状态观测：NEW、RUNNABLE、BLOCKED、WATTING、TIMED_WATTING、TERMINATED
 */

public class ThreadStatusState {

public static void main(String[] args) throws InterruptedException {
	// main 方法
	Thread thread = new Thread(() -> {
		for (int i = 0; i < 5; i++) {
			try {
				// TIMED_WAITING：正在等待另一个先后测个执行特定动作的线程处于此状态
				// BLOCKED：被阻塞等待监视器锁定的线程处于此状态
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		System.out.println("///////");
	});
	
	// 观察状态
	Thread.State state = thread.getState();
	
	// NEW：尚未启动的线程处于此状态
	System.out.println(state);
	
	// 观察启动后
	thread.start();
	state = thread.getState();
	// Runnable：在 Java 虚拟机中执行的线程处于此状态
	System.out.println(state);
	
	// TERMINATED：已退出的线程处于此状态
	while (state != Thread.State.TERMINATED) {
		Thread.sleep(100);
		// 更新线程状态
		state = thread.getState();
		// 输出状态
		System.out.println(state);
	}
	
	// 线程停止后不能再次启动，否则会报错 Exception in thread "main" java.lang.IllegalThreadStateException
	thread.start();
}
}

class TempThreadStatusState {
// 空类
}