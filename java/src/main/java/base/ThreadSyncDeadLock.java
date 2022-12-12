package base;

/**
 * @file base.ThreadSyncDeadLock
 * @author crisimple
 * @date 2020/8/27 12:34 上午
 * @description 死锁
 * 多个线程互相持有对方需要的资源，然后形成僵持
 */

public class ThreadSyncDeadLock {

public static void main(String[] args) {
	// main 方法
	Makeup makeup1 = new Makeup(0, "A");
	Makeup makeup2 = new Makeup(1, "B");
	
	makeup1.start();
	makeup2.start();
}
}

class Lipstick {
	
}

class Mirror {
	
}

class Makeup extends Thread {
// 需要的资源只有一份，用 static 来保证只有一份
static Lipstick lipstick = new Lipstick();
static Mirror mirror = new Mirror();

// 定义选择
int choose;
// 使用化妆品的人
String name;

// 有参构造器
public Makeup(int choose, String name) {
	this.choose = choose;
	this.name = name;
}

@Override
public void run() {
	// 化妆
	try {
		makeup();
	} catch (InterruptedException e) {
		e.printStackTrace();
	}
}

public void makeup() throws InterruptedException {
	if(choose == 0) {
		// 获得口红的锁
		synchronized(lipstick) {
			System.out.println(this.name + "获得口红的锁");
			Thread.sleep(1000);
			// 一秒钟后获得镜子的锁
			synchronized(mirror) {
				System.out.println(this.name + "获得镜子的锁");
			}
		}
	} else {
		// 获得镜子的锁
		synchronized(mirror) {
			System.out.println(this.name + "获得镜子的锁");
			Thread.sleep(1000);
			// 一秒钟后获得口红的锁
			synchronized(lipstick) {
				System.out.println(this.name + "获得口红的锁");
			}
		}
		
		/***
		 * 解决死锁的方法，将锁拿出来不要持有别人的锁
		 */
//            synchronized(lipstick){
//                    System.out.println(this.name + "获得口红的锁");
//            }
	}
}
}