package com.secoder.base; /**
 * @file ThreadDownloaderRunnable
 * @author crisimple
 * @date 2020/8/24 11:25 上午
 * @description 通过继承 Runnable 接口实现多线程下载网图
 */

//import org.apache.commons.io.FileUtils;

//import org.apache.tomcat.util.http.fileupload.FileUtils;

public class ThreadRunnableDownloader implements Runnable {

private String url;
private String name;

public ThreadRunnableDownloader(String url, String name) {
	this.url = url;
	this.name = name;
}

public static void main(String[] args) {
	ThreadRunnableDownloader t1 = new ThreadRunnableDownloader("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3160036411,2748896368&fm=26&gp=0.jpg", "images\1.jpg");
	ThreadRunnableDownloader t2 = new ThreadRunnableDownloader("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3160036411,2748896368&fm=26&gp=0.jpg", "images\2.jpg");
	ThreadRunnableDownloader t3 = new ThreadRunnableDownloader("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3160036411,2748896368&fm=26&gp=0.jpg", "images\3.jpg");
	new Thread(t1).start();
	new Thread(t2).start();
	new Thread(t3).start();
}

@Override
public void run() {
	RunnableWebDownloader runnableWebDownloader = new RunnableWebDownloader();
	runnableWebDownloader.downLoader(url, name);
	System.out.println("网图" + name + "被下载了！");
}
}

/**
 *
 */
class RunnableWebDownloader {
public void downLoader(String url, String name) {
	//try {
	//	//FileUtils.copyURLToFile(new URL(url), new File(name));
	//} catch (IOException e) {
	//	System.out.println("downLoader() 方法下载失败，请检查！");
	//	e.printStackTrace();
	//} finally {
	//	System.out.println("!!网图下载程序执行完毕!！");
	//}
}
}
