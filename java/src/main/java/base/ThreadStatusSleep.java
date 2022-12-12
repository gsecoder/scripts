package base;/*
 * @file base.ThreadStatusSleep
 * @author sf
 * @date 2020/8/25 3:41 下午
 * @description 线程休眠
 * 应用：
 *      1. 模拟网络延时，方法问题的发生
 *      2. 模拟倒计时
 */

import java.text.SimpleDateFormat;
import java.util.Date;

public class ThreadStatusSleep {

public static void main(String[] args) {
	/**
	 * 10 秒倒计时
	 */
	timeDown();
	
	/**
	 * 打印系统时间
	 */
	printSysTime();
}

public static void timeDown() {
	int num = 10;
	while (true) {
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		System.out.println(num--);
		if(num <= 0) {
			break;
		}
	}
}

public static void printSysTime() {
	// 获取系统当前时间
	Date startTime = new Date(System.currentTimeMillis());
	
	while (true) {
		try {
			Thread.sleep(1000);
			System.out.println(new SimpleDateFormat("HH:mm:ss").format(startTime));
			// 更新当前时间
			startTime = new Date(System.currentTimeMillis());
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
}

class TempThreadStatusSleep {
// 空类
}
