package aop_realization_three;

import aop_realization_three.aop_annotation.UserService;
import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * @Author secoder
 * @File AnnotationPointcutTest
 * @Time 2021-07-22 19:19
 * @Description
 */
public class AnnotationPointcutTest {
	
	@Test
	public void test(){
		ApplicationContext context = new ClassPathXmlApplicationContext("aop_realization_three/annotation_point_cut.xml");
		UserService userService = (UserService) context.getBean("userService");
		userService.query();
	}
}
