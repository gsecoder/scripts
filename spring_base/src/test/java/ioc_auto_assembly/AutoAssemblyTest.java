package ioc_auto_assembly;

import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * @Author crisimple
 * @File AutoAssemblyTest
 * @Time 2021-03-28 09:36
 * @Description
 */
public class AutoAssemblyTest {

    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("ioc_auto_assembly.xml");

    @Test
    public void autoAssemblyTest(){
       User user = (User) applicationContext.getBean("user");
       user.getCat().shout();
       user.getDog().shout();
    }
}
