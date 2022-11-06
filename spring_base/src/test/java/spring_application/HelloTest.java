package spring_application;

/**
 * @Author sf
 * @File HelloTest
 * @Time 2021-03-24 20:17
 * @Description
 */
import org.junit.jupiter.api.Test;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class HelloTest {
	
	@Test
	public void helloTest(){
		// 解析beans.xml文件 , 生成管理相应的Bean对象
		ClassPathXmlApplicationContext classPathXmlApplicationContext = new ClassPathXmlApplicationContext("spring_application.xml");
		
		// getBean：参数即为Spring配置文件中的bean的id：
		Hello hello = (Hello) classPathXmlApplicationContext.getBean("hello");
		hello.show();
	}
}