package ioc_spring_config;

import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * @Author secoder
 * @File UserTest
 * @Time 2021-07-20 20:49
 * @Description
 */
public class UserTest {
	
	@Test
	public void userTest(){
		ApplicationContext context = new ClassPathXmlApplicationContext("ioc_spring_config/ioc_spring_config.xml");
		
		// 在执行getBean的时候，user已经创建好了（也就是我们bean中的id），通过无参构造
		User user = (User) context.getBean("userAlias");
		
		// 调用对象的方法，结果可以发现，在调用show方法之前，User对象已经通过无参构造初始化了！
		user.show();
	}
	
}
