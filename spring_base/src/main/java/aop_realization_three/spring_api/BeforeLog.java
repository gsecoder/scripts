package aop_realization_three.spring_api;

import org.springframework.aop.MethodBeforeAdvice;

import java.lang.reflect.Method;

/**
 * @Author secoder
 * @File Log
 * @Time 2021-07-22 15:29
 * @Description
 */
public class BeforeLog implements MethodBeforeAdvice {
	
	/**
	 * method: 要执行的目标对象的方法
	 * objects: 被调用的方法的参数
	 * Object: 目标对象
	 */
	@Override
	public void before(Method method, Object[] args, Object target) throws Throwable {
		System.out.println(target.getClass().getName() + "的" + method.getName() + "方法被执行了");
	}
}
