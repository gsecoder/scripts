package com.secoder.base;

/**
 * @file ThreadTorRabbit
 * @author sf
 * @date 2020/8/24 2:54 下午
 * @description 通过线程
 */

public class ThreadTorRabbit implements Runnable {
// 赢家标志位
private static String winner;

@Override
public void run() {
	for (int i = 0; i <= 1_000_000; i++) {
		// 模拟兔子休息
		if(Thread.currentThread().getName().equals("兔子") && i % 20 == 0) {
			try {
				Thread.sleep(1);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		
		// 判断比赛是不是结束了
		boolean flag = gameOver(i);
		//如果比赛结束了，停止程序
		if(flag) {
			break;
		}
		System.out.println(Thread.currentThread().getName() + "-->跑了" + i + "步");
	}
}

private boolean gameOver(int steps) {
	// 判断是否有胜利者
	if(winner != null) {
		return true;
	} else {
		if(steps >= 100) {
			winner = Thread.currentThread().getName();
			System.out.println("winner is:" + winner);
			return true;
		}
	}
	return false;
}

public static void main(String[] args) {
	// main 方法
	new Thread(new ThreadTorRabbit(), "兔子").start();
	new Thread(new ThreadTorRabbit(), "乌龟").start();
}
}

class TempThreadTorRabbit {
// 空类
}
