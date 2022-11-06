/**
 * @file ThreadProxy
 * @author sf
 * @date 2020/8/24 8:11 下午
 * @description 静态代理
 * 要求：
 * 真实对象和代理对象都要实现同一个接口
 * 代理对象要代理真实角色
 * 好处：
 * 代理对象可以做很多真实对象做不了的事情
 * 真实对象专注做自己的事情
 */

public class ThreadProxy {

public static void main(String[] args) {
	WeddingCompany weddingCompany = new WeddingCompany(new Your());
	weddingCompany.HappyMarry();
}
}

interface Marry {
void HappyMarry();
}


/**
 * 我是真实角色，主角去结婚
 */
class Your implements Marry {
@Override
public void HappyMarry() {
	System.out.println("我要结婚了，超开心！");
}
}

/**
 * 代理角色婚庆公司，帮助你去办理结婚事务
 */
class WeddingCompany implements Marry {
private Marry target;

public WeddingCompany(Marry target) {
	this.target = target;
}

@Override
public void HappyMarry() {
	before();
	this.target.HappyMarry();
	after();
}

public void before() {
	System.out.println("结婚前准备");
}

public void after() {
	System.out.println("结婚后付尾款");
}
}