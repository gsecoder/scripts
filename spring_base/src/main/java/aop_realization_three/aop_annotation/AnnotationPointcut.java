package aop_realization_three.aop_annotation;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Before;
import org.springframework.scheduling.annotation.Async;

/**
 * @Author secoder
 * @File AnnotationPointcut
 * @Time 2021-07-22 17:59
 * @Description
 */
@Async
public class AnnotationPointcut {
	
	@Before("execution(* aop_realization_three.aop_annotation.UserServiceImpl.*(..))")
	public void before(){
		System.out.println("--------- 方法执行前 -------------");
	}
	
	@After("execution(* aop_realization_three.aop_annotation.UserServiceImpl.*(..))")
	public void after(){
		System.out.println("--------- 方法执行后 -------------");
	}
	
	@Around("execution(* aop_realization_three.aop_annotation.UserServiceImpl.*(..))")
    public void around(ProceedingJoinPoint jp) throws Throwable {
        System.out.println("环绕前");
        System.out.println("签名:"+jp.getSignature());
        //执行目标方法proceed
        Object proceed = jp.proceed();
        System.out.println("环绕后");
        System.out.println(proceed);
    }
}
