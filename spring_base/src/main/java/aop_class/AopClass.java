package aop_class;

/**
 * @Author crisimple
 * @File AopClass
 * @Time 2021-04-03 18:50
 * @Description
 */
public class AopClass {

    public void before(){
        System.out.println("...自定义类来实现AOP，在方法前执行...");
    }

    public void after(){
        System.out.println("...自定义类来实现AOP，在方法后执行...");
    }
}
