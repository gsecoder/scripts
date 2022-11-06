package static_proxy;

/**
 * @Author sf
 * @File Tenant
 * @Time 2021-03-31 18:05
 * @Description 租房者
 *  在这个过程中，你直接接触的就是中介，就如同现实生活中的样子，你看不到房东，但是你依旧租到了房东的房子通过代理，
 *  这就是所谓的代理模式，程序源自于生活，所以学编程的人，一般能够更加抽象的看待生活中发生的事情。
 */
public class Tenant {
	
	public static void main(String args[]){
		// 房东要出租房
		LandlordA landlordA = new LandlordA();
		// 中介帮房东租房
		LandordProxy landordProxy = new LandordProxy(landlordA);
		// 找中介
		landordProxy.rent();
		
		
		// UserService 业务
		UserServiceImpl userService = new UserServiceImpl();
		//代理类
        UserServicesProxy proxy = new UserServicesProxy();
		//使用代理类实现日志功能！
		proxy.setUserServiceImpl(userService);
 
        proxy.adds();
        
	}
}
