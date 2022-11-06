/**
 * @file ThreadStatusDaemon
 * @author sf
 * @date 2020/8/25 8:31 下午
 * @description 线程分为 用户线程 和 守护线程
 * 虚拟机必须确保 用户线程 执行完毕；虚拟机不用等待守护线程执行完毕
 * 守护线程：后台操作日志、监控内存、垃圾回收等
 */

public class ThreadStatusDaemon {

public static void main(String[] args) {
	// main 方法
	
	God god = new God();
	You you = new You();
	
	Thread thread = new Thread(god);
	// 默认是 false，表示是用户线程，正常的线程都是用户线程...
	thread.setDaemon(true);
	thread.start();
	
	// 你就是个用户线程
	new Thread(you).start();
}
}

class God implements Runnable {
@Override
public void run() {
	System.out.println("God bless You");
}
}

class You implements Runnable {
@Override
public void run() {
	for (int i = 0; i < 36500; i++) {
		System.out.println("开心😸活着的第: " + i + " 天");
	}
	System.out.println("GoodBye World");
}
}
