/**
 * @file ThreadRealizationImplementsRunnable
 * @author sf
 * @date 2020/8/24 10:52 上午
 * @description 通过实现 Runnable 接口实现多线程
 * 避免单继承局限性，灵活方便，方便同一对象被多个线程使用
 */

public class ThreadRealizationImplementsRunnable implements Runnable {

public static void main(String[] args) {
	
	// 调用子线程重写后的方法
//        Thread t1 = new Thread(new ThreadRealizationImplementsRunnable());
//        t1.start();
	// 也可以使用匿名类来调用匿名方法
	new Thread(new ThreadRealizationImplementsRunnable()).start();
	
	// main 方法
	for (int i = 0; i < 1000; i++) {
		System.out.println("我是main方法里的主线程：我在跑主线程。");
	}
}

@Override
public void run() {
	for (int i = 0; i < 20; i++) {
		System.out.println("我是子线程：我在重写 Runnable 的 run() 方法。");
	}
}
}

class TempRunnable {
	
}