package aop_static_proxy;

/**
 * @Author secoder
 * @File Proxy
 * @Time 2021-07-21 20:04
 * @Description
 */
public class Proxy implements Rent{
	
	private Host host;
	
	public Proxy(){}
	// 房东把房委托给中介进行出租
	public Proxy(Host host){
		this.host = host;
	}
	
	// 租房
	public void rent(){
		System.out.println("带租客看房");
	}
	
	// 收取中介费
	public void fare(){
		System.out.println("收取中介费");
	}
	
}
