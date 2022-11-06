package ioc_di_scope;

import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * @Author sf
 * @File DiScopeTest
 * @Time 2021-03-27 18:56
 * @Description
 */
public class DiScopeTest {
	
	ApplicationContext applicationContext = new ClassPathXmlApplicationContext("ioc_di_scope.xml");
	
	// Singleton范围	
	@Test
	public void diScopeSingletonTest(){
		DiScopeSingleton diScope = (DiScopeSingleton) applicationContext.getBean("diScopeSingleton");
		System.out.println(diScope.getName());
		
		// 测试在单例模式，单例是一样的
		DiScopeSingleton diScope1 = (DiScopeSingleton) applicationContext.getBean("diScopeSingleton");
		System.out.println("diScope == diScope1：" + (diScope == diScope1));
	}
	
	// Prototype 范围
    @Test
	public void diScopePrototypeTest(){
		DiScopePrototype diScope = (DiScopePrototype) applicationContext.getBean("diScopePrototype");
		DiScopePrototype diScope1 = (DiScopePrototype) applicationContext.getBean("diScopePrototype");
	    System.out.println("diScope == diScope1：" + (diScope == diScope1));
    }
    
    /**
    // Request 范围
	@Test
	public void diScopeRequestTest(){
		DiScopeWeb diScope = (DiScopeWeb) applicationContext.getBean("diScopeRequest");
		DiScopeWeb diScope1 = (DiScopeWeb) applicationContext.getBean("diScopeRequest");
	    System.out.println("diScope == diScope1：" + (diScope == diScope1));
    }
    
    // Session 范围
	@Test
	public void diScopeSessionTest(){
		DiScopeWeb diScope = (DiScopeWeb) applicationContext.getBean("diScopeSession");
		DiScopeWeb diScope1 = (DiScopeWeb) applicationContext.getBean("diScopeSession");
	    System.out.println("diScope == diScope1：" + (diScope == diScope1));
    }
	*/
}
