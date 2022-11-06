package aop_realization_three;

import aop_realization_three.spring_api.UserService;
import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * @Author secoder
 * @File UserServiceTest
 * @Time 2021-07-22 16:35
 * @Description
 */
public class UserServiceTest {
	
	@Test
	public void test(){
		ApplicationContext context = new ClassPathXmlApplicationContext("aop_realization_three/spring_api.xml");
		UserService userService = (UserService) context.getBean("userService");
		userService.query();
	}
}
