package service;

import ioc_dao.UserDaoMysqlImpl;
import ioc_dao.UserDaoSQLServerImpl;
import ioc_service.UserServiceImpl;
import org.junit.jupiter.api.Test;

public class GetUserTest {

	/**
	 * 未采用IOC方式的获取用户方法
	 */
	public void getUser1Test(){
		UserServiceImpl userService = new UserServiceImpl();
		userService.getUser();
	}

	/**
	 * 采用IOC方式获取用户的方法，这里的测试就是模拟用户，通过用户的选择来选择通过哪种数据库获取用户数据
	 *  
	 *  现在是由我们自行控制创建对象 , 把主动权交给了调用者 . 程序不用去管怎么创建,怎么实现了 . 它只负责提供一个接口 .
	 *  
	 *  这种思想, 从本质上解决了问题, 我们程序员不再去管理对象的创建了 , 更多的去关注业务的实现 . 耦合性大大降低 . 这也就是IOC的原型 !
	 */
	@Test
	public void getUser2Test(){
		UserServiceImpl userService = new UserServiceImpl();
		
		// 通过MYSQL获取数据
		userService.setUserDao(new UserDaoMysqlImpl());
		userService.getUser();
		
		// 通过SQLServer获取数据
		userService.setUserDao(new UserDaoSQLServerImpl());
		userService.getUser();
	}
	
}
