package aop_annotation;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;

/**
 * @Author crisimple
 * @File AopAnnotation
 * @Time 2021-04-03 19:17
 * @Description
 */
@Aspect
public class AopAnnotation {

    @Before("execution(* aop.AopServiceImpl.*(..))")
    public void before(){
        System.out.println("---------AopAnnotation 方法执行前---------");
    }

    @After("execution(* aop.AopServiceImpl.*(..))")
    public void after(){
        System.out.println("---------AopAnnotation 方法执行后---------");
    }

    public void around(ProceedingJoinPoint proceedingJoinPoint) throws Throwable{
        System.out.println("环绕前");
        System.out.println("签名：" + proceedingJoinPoint.getSignature());

        // 执行目标方法processed
        Object proceed = proceedingJoinPoint.proceed();
        System.out.println("环绕后");
        System.out.println(proceed);
    }
}
