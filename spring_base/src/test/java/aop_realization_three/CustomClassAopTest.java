package aop_realization_three;

import aop_realization_three.custom_class_aop.UserService;
import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * @Author secoder
 * @File CustomAopTest
 * @Time 2021-07-22 17:23
 * @Description
 */
public class CustomClassAopTest {
	
	@Test
	public void test(){
		ApplicationContext context = new ClassPathXmlApplicationContext("aop_realization_three/custom_class_aop.xml");
		UserService userService = (UserService) context.getBean("userService");
		userService.query();
	}
}
