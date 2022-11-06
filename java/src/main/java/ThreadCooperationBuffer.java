/**
 * @file ThreadCooperationBuffer
 * @author sf
 * @date 2020/8/27 1:27 上午
 * @description 生产者消费者模型 --- 利用缓冲区来解决（管程法）
 */

public class ThreadCooperationBuffer {

public static void main(String[] args) {
	// main 方法
	Container container = new Container();
	new Producer(container).start();
	new Customer(container).start();
}
}

/**
 * 生产者
 */
class Producer extends Thread {
Container container;

public Producer(Container container) {
	this.container = container;
}

/**
 * 生产
 */
@Override
public void run() {
	for (int i = 0; i < 100; i++) {
		container.push(new Goods(i));
		System.out.println("生产了" + i + "个");
	}
}
}


/**
 * 消费者
 */
class Customer extends Thread {
Container container;

public Customer(Container container) {
	this.container = container;
}

/**
 * 消费
 */
@Override
public void run() {
	for (int i = 0; i < 100; i++) {
		System.out.println("【消费了】-->" + container.pop().id + "个");
	}
}
}


/**
 * 产品
 */
class Goods {
int id;

public Goods(int id) {
	this.id = id;
}
}


class Container {

// 需要一个容器大小
Goods[] goodses = new Goods[10];
// 计数器
int count = 0;

// 生产者放入产品
public synchronized void push(Goods goods) {
	if(count == goodses.length) {
		// 通知消费者，生产等待
		try {
			this.wait();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
	}
	
	// 如果没有满
	goodses[count] = goods;
	count++;
	
	// 通知消费者消费
	this.notifyAll();
}

// 消费者消费
public synchronized Goods pop() {
	// 判断是否可以消费
	if(count == 0) {
		// 等待生产者生产，消费者等待
		try {
			this.wait();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	// 可以消费
	count--;
	Goods goods = goodses[count];
	
	// 吃完了，通知生产者生产
	this.notifyAll();
	return goods;
}
}