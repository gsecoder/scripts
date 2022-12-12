package base;/*
 * @file base.ThreadDownloader
 * @author sf
 * @date 2020/8/23 5:14 下午
 * @description 多线程线程下载网图
 */

//import org.apache.commons.io.FileUtils;

public class ThreadDownloader extends Thread {

public static void main(String[] args) {
	// main 方法
	ThreadDownloader t1 = new ThreadDownloader("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3160036411,2748896368&fm=26&gp=0.jpg", "images/1.jpg");
	ThreadDownloader t2 = new ThreadDownloader("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3160036411,2748896368&fm=26&gp=0.jpg", "images/2.jpg");
	ThreadDownloader t3 = new ThreadDownloader("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3160036411,2748896368&fm=26&gp=0.jpg", "images/3.jpg");
	t1.start();
	t2.start();
	t3.start();
}

// 网络图片地址
private String url;
// 文件名
private String name;

public ThreadDownloader(String url, String name) {
	this.url = url;
	this.name = name;
}

@Override
public void run() {
	WebDownloader webDownloader = new WebDownloader();
	//webDownloader.downLoader(url, name);
	System.out.println("网图" + name + "下载成功了");
}
}

/**
 * 实例：使用多线程下载网图
 */
class WebDownloader {
/**
 * 网图下载方法
 *
 * @param url
 * @param name
 */
//public void downLoader(String url, String name) {
//	try {
//		FileUtils.copyURLToFile(new URL(url), new File(name));
//	} catch (IOException e) {
//		System.out.println("文件下载失败，downLoader方法报错");
//		e.printStackTrace();
//	}
//}
}