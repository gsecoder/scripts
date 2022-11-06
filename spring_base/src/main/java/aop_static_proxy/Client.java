package aop_static_proxy;

/**
 * @Author secoder
 * @File Client
 * @Time 2021-07-21 20:09
 * @Description 租客，租客一般去找代理
 */
public class Client {
	
	public static void main(String[] args){
		// 房东要租房
		Host host = new Host();
		// 中介帮助房东
		Proxy proxy = new Proxy(host);

		// 你去找中介租房
		proxy.rent();

	}
}
