package base;

import java.util.Scanner;

public class ProcessScanner {
public static void main(String[] args) {
	// 创建一个扫描器对象，用于接受键盘数据
	Scanner scanner = new Scanner(System.in);
	System.out.println("（1）使用 next 方式接受：");
	// 判断用户有没有输入
	if(scanner.hasNext()) {
		// 使用 next 方式接收，程序会等待用户输入完毕
		String str = scanner.next();
		System.out.println("    （1）输出的内容为：" + str);
		
		System.out.println("（2）使用 nextLine 方式接受：");
		String str2 = scanner.nextLine();
		System.out.println("    （2）输出的内容为：" + str2);
		
		// 凡是属于 IO 流的类如果不关闭会一直占用资源
		scanner.close();
	}
	
}
	
}