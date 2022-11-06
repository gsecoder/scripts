/*
 * @file ThreadSyncUnsafeTakeMoney
 * @author sf
 * @date 2020/8/26 7:35 下午
 * @description
 *      线程同步不安全取钱
 */

public class ThreadSyncUnsafeTakeMoney {

public static void main(String[] args) {
	// main 方法
	
	Account account = new Account(100, "结婚基金");
	
	TakeMoney you = new TakeMoney(account, 10, "你自己");
	TakeMoney wife = new TakeMoney(account, 20, "你妻子");
	
	you.start();
	wife.start();
}
}

/**
 * 银行账户
 */
class Account {
// 账户金额
int money;
// 账户卡名
String cardName;

public Account(int money, String cardName) {
	this.money = money;
	this.cardName = cardName;
}
}

/**
 * 模拟取款业务
 */
class TakeMoney extends Thread {

// 银行账户对象
Account account;
// 取了多少钱
int takingMoney;
// 手上有多少钱
int localMoney;

public TakeMoney(Account account, int takingMoney, String cardName) {
	super(cardName);
	this.account = account;
	this.takingMoney = takingMoney;
}

@Override
public void run() {
	// synchronized 默认的是 this，取钱的对象
	synchronized(account) {
		// 判断是否有钱
		if((account.money - takingMoney) < 0) {
			System.out.println(Thread.currentThread().getName() + "钱不够花了...");
			return;
		}
		
		// sleep 可以放大问题的发生性
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		// 卡里的余额
		account.money = account.money - takingMoney;
		System.out.println(account.cardName + "卡里的余额为：" + account.money);
		
		// 手上的钱
		localMoney = localMoney + takingMoney;
		// Thread.currentThread().getName() 全等于 this.getName()
		System.out.println(this.getName() + "手里的钱为：" + localMoney);
	}
	
}
}