package aop;

import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * @Author crisimple
 * @File AopTest
 * @Time 2021-04-03 18:26
 * @Description
 */
public class AopTest {

    @Test
    public void aopFileTest(){
        ApplicationContext applicationContext =  new ClassPathXmlApplicationContext("aop_file.xml");
        AopService aopService = (AopService) applicationContext.getBean("aopService");
        aopService.add();
    }

    @Test
    public void aopClassTest(){
        ApplicationContext applicationContext =  new ClassPathXmlApplicationContext("aop_class.xml");
        AopService aopService = (AopService) applicationContext.getBean("aopService");
        aopService.add();
    }

    @Test
    public void aopAnnotationTest(){
        ApplicationContext applicationContext =  new ClassPathXmlApplicationContext("aop_annotation.xml");
        AopService aopService = (AopService) applicationContext.getBean("aopService");
        aopService.add();
    }
}
