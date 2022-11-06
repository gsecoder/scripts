package ioc_annotation;

import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
/**
 * @Author sf
 * @File UserTest
 * @Time 2021-03-29 21:45
 * @Description
 */
public class AnnotationTest {
	
	ApplicationContext applicationContext = new ClassPathXmlApplicationContext("ioc_annotation.xml");

	@Test
	public void person1Test(){
		Person person = (Person) applicationContext.getBean("person");
		System.out.println(person.name);
	}
	
	@Test
    public void userTest(){
		User user = (User) applicationContext.getBean("user");
		System.out.println(user.getDog());
	}
	
	@Test
	public void userNameTest(){
		User user = (User) applicationContext.getBean("user");
		System.out.println("user.name: " + user.name);
	}
	
	@Test
	public void userStrTest(){
		User user = (User) applicationContext.getBean("user");
		System.out.println("user.str" + user.getStr());
	}
	
	@Test
	public void person2Test(){
		Person person = (Person) applicationContext.getBean("person");
		System.out.println(person.getAge());
		System.out.println(person.getSex());
	}
	
	@Test
	public void myConfigTest(){
		ApplicationContext applicationContext = new AnnotationConfigApplicationContext(MyConfig.class);
		ConfigBase configBase = (ConfigBase) applicationContext.getBean("configBase");
		System.out.println(configBase.name);
	}
}
