package dependency_injection;

import ioc_dependency_injection.Student;
import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * @Author sf
 * @File StudentTest
 * @Time 2021-03-27 11:15
 * @Description
 */
public class StudentTest {
	ApplicationContext applicationContext = new ClassPathXmlApplicationContext("dependency_injection.xml");
	
	@Test
	public void studentConstTest(){
		Student student = (Student) applicationContext.getBean("studentConst");
		System.out.println(student.getName());
	}
	
	@Test
	public void studentBeanTest(){
		Student student = (Student) applicationContext.getBean("studentBean");
		System.out.println(student.getName() + "住在【" + student.getAddress() + "】");
	}
	
	@Test
	public void studentArrayTest(){
		Student student = (Student) applicationContext.getBean("studentArray");
		System.out.println(student.getName() + "住在【" + student.getAddress() + "】" + ", 喜欢的书有：" + student.getBooks());
	}
	
	@Test
	public void studentListTest(){
		Student student = (Student) applicationContext.getBean("studentList");
		System.out.println(student.getName() + "的爱好有：" + student.getHobbies());
	}
	
	@Test
	public void studentMapTest(){
		Student student = (Student) applicationContext.getBean("studentMap");
		System.out.println(student.getName() + "的银行卡有：" + student.getCard());
	}
	
	@Test
	public void studentSetTest(){
		Student student = (Student) applicationContext.getBean("studentSet");
		System.out.println(student.getName() + "喜欢玩：" + student.getGames());
	}
	
	@Test
	public void studentNullTest(){
		Student student = (Student) applicationContext.getBean("studentNull");
		System.out.println(student.getName() + "的妻子是：" + student.getWife());
	}
	
	@Test
	public void studentPropertiesTest(){
		Student student = (Student) applicationContext.getBean("studentProperties");
		System.out.println(student.getName() + "的详细信息是：" + student.getInfo());
	}
}
