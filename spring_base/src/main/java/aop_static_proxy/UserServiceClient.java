package aop_static_proxy;

/**
 * @Author secoder
 * @File UserServiceTest
 * @Time 2021-07-21 20:38
 * @Description
 */
public class UserServiceClient {
	
	// Failed to execute goal org.codehaus.mojo:exec-maven-plugin:3.0.0:exec (default-cli) on project spring_base: Command execution failed.
	// 主类加Test的时候。这里测试不要用main方法测试，使用junit测试（在test目录下）
	//@Test
	//public void userServiceTest(){
	public static void main(String[] args) {
		// 真实业务
		UserServiceImpl userServiceImpl = new UserServiceImpl();
		// 代理类
		UserServiceProxy proxy = new UserServiceProxy();
		// 使用代理类实现日志功能
		proxy.setUserService(userServiceImpl);
		
		proxy.add();
	}
}
