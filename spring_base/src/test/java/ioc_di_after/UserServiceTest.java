package ioc_di_after;

import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * @Author secoder
 * @File UserServiceTest
 * @Time 2021-07-19 19:48
 * @Description
 */
public class UserServiceTest {
	
	@Test
	public void userServiceTest(){
		UserService userService = new UserServiceImpl();
		userService.getUser();
	}
	
	@Test
	public void userServiceTest2(){
		ApplicationContext applicationContext = new ClassPathXmlApplicationContext("ioc_di_after/ioc_di_after.xml");
		UserServiceImpl userService = (UserServiceImpl) applicationContext.getBean("ServiceImpl");
		userService.getUser();
	}
}
