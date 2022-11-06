package ioc_create_object;

import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * @Author secoder
 * @File UserTTest
 * @Time 2021-03-24 21:36
 * @Description
 */
public class UserTTest {
	
	@Test
	public void userTTest(){
		ApplicationContext applicationContext = new ClassPathXmlApplicationContext("ioc_create_object.xml");
		UserT userT1 = (UserT) applicationContext.getBean("userT1");
		UserT userT2 = (UserT) applicationContext.getBean("userT2");
		UserT userT3 = (UserT) applicationContext.getBean("userT3");
		userT1.show();
		userT2.show();
		userT3.show();
	}
}
