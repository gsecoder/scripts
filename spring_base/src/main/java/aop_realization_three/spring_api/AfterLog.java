package aop_realization_three.spring_api;

import org.springframework.aop.AfterReturningAdvice;

import java.lang.reflect.Method;

/**
 * @Author secoder
 * @File AfterLog
 * @Time 2021-07-22 15:32
 * @Description
 */
public class AfterLog implements AfterReturningAdvice {
	
	/**
	 * method: 要执行的目标对象的方法
	 * objects: 被调用的方法的参数
	 * Object: 目标对象
	 */
	@Override
	public void afterReturning(Object returnValue, Method method, Object[] args, Object target) throws Throwable {
		System.out.println("执行了" + target.getClass().getName() + "的" + method.getName() + "方法，的返回值" + returnValue);
	}
}
