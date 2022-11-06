package aop_log;

import org.springframework.aop.MethodBeforeAdvice;

import java.lang.reflect.Method;

/**
 * @Author crisimple
 * @File Log
 * @Time 2021-04-03 18:05
 * @Description
 */
public class BeforeLog implements MethodBeforeAdvice {

    /**
     *
     * @param method 要执行的目标对象的方法
     * @param objects 被调用的方法的参数
     * @param o 目标对象
     * @throws Throwable
     */
    @Override
    public void before(Method method, Object[] objects, Object o) throws Throwable {
        System.out.println(o.getClass().getName() + "的" + method.getName() + "方法被执行了");
    }
}
