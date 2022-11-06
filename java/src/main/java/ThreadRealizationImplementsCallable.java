/**
 * @file ThreadRealizationImplementsCallable
 * @author sf
 * @date 2020/8/24 7:29 下午
 * @description 线程实现方法三，继承接口 Callable 接口
 * 可以定义返回值
 * 可以抛出异常
 */

import java.util.concurrent.*;

public class ThreadRealizationImplementsCallable implements Callable<Boolean> {

private String url;
private String name;

public ThreadRealizationImplementsCallable(String url, String name) {
	this.url = url;
	this.name = name;
}

/**
 *
 */
@Override
public Boolean call() {
	WebDownloader webDownloader = new WebDownloader();
	//webDownloader.downLoader(url, name);
	System.out.println("网图" + name + "下载成功了");
	return true;
}

public static void main(String[] args) {
	// main 方法
	ThreadRealizationImplementsCallable t1 = new ThreadRealizationImplementsCallable("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3160036411,2748896368&fm=26&gp=0.jpg", "images/1.jpg");
	ThreadRealizationImplementsCallable t2 = new ThreadRealizationImplementsCallable("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3160036411,2748896368&fm=26&gp=0.jpg", "images/2.jpg");
	ThreadRealizationImplementsCallable t3 = new ThreadRealizationImplementsCallable("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3160036411,2748896368&fm=26&gp=0.jpg", "images/3.jpg");
	
	// 创建执行服务
	ExecutorService ser = Executors.newFixedThreadPool(1);
	
	// 提交执行
	Future<Boolean> r1 = ser.submit(t1);
	Future<Boolean> r2 = ser.submit(t2);
	Future<Boolean> r3 = ser.submit(t3);
	
	// 获取结果
	try {
		boolean rs1 = r1.get();
		System.out.println("rs1: " + rs1);
	} catch (InterruptedException e) {
		e.printStackTrace();
	} catch (ExecutionException e) {
		e.printStackTrace();
	}
	try {
		boolean rs2 = r2.get();
	} catch (InterruptedException e) {
		e.printStackTrace();
	} catch (ExecutionException e) {
		e.printStackTrace();
	}
	try {
		boolean rs3 = r3.get();
	} catch (InterruptedException e) {
		e.printStackTrace();
	} catch (ExecutionException e) {
		e.printStackTrace();
	}
	
	// 关闭服务
	ser.shutdown();
}
}

class TempThreadRealizationImplementsCallable {
// 空类
}
