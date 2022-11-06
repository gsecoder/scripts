package aop_dynamic_proxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

/**
 * @Author secoder
 * @File ProxyInvocationHandler
 * @Time 2021-07-21 23:22
 * @Description 动态代理
 */
public class ProxyInvocationHandler implements InvocationHandler {

    private Rent rent;
    private Object target;

    public void setRent(Rent rent){
        this.rent = rent;
    }

    // 生成通用代理类
    public void setTarget(Object target) {
        this.target = target;
    }

    // 生成代理类，重点是第二个参数，获取要代理的抽象角色！之前都是一个角色，现在可以代理一类角色
    public Object getProxy(){
        return Proxy.newProxyInstance(
                this.getClass().getClassLoader(),
                rent.getClass().getInterfaces(),this);
    }

    // Proxy：代理类method：代理类的调用处理程序的方法对象
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable{
        setHouse();

        // 核心：本质利用反射实现
        Object result = method.invoke(rent, args);
        fare();
        return result;
    }

    // 看房
    public void  setHouse(){
        System.out.println("带房客看房");
    }

    // 收中介费
    public void fare(){
        System.out.println("收中介费");
    }
}
