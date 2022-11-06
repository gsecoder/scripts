package cp_namespace;

import ioc_cp_namespace.CP;
import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * @Author sf
 * @File CPTest
 * @Time 2021-03-29 15:07
 * @Description
 */
public class CPTest {
	
	ApplicationContext applicationContext = new ClassPathXmlApplicationContext("cp_namespace.xml");
	
	@Test
	public void pTest(){
		CP cp = (CP) applicationContext.getBean("userP");
		System.out.println(cp.toString());
	}
	
	@Test
	public void cTest(){
		CP cp = (CP) applicationContext.getBean("userC");
		// 这有个问题还未排查到，不知道为啥c注入获取不到name的值，获取到的值为null
		System.out.println(cp);
	}
}
