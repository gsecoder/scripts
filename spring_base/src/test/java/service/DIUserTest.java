package service;

import ioc_service.UserService;
import org.junit.jupiter.api.Test;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * @Author sf
 * @File DIUserTest
 * @Time 2021-03-24 20:54
 * @Description
 */
public class DIUserTest {
	
	@Test
	public void diUserTest(){
		ClassPathXmlApplicationContext classPathXmlApplicationContext = new ClassPathXmlApplicationContext("ioc_spring_config/other_ioc_config.xml");
		UserService userService = (UserService) classPathXmlApplicationContext.getBean("ServiceImpl");
		userService.getUser();
	}
}
