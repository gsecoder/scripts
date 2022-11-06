package aop_dynamic_proxy;

import aop_static_proxy.ProxyLog;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

/**
 * @Author secoder
 * @File ProxyInvocationHandlerCommon
 * @Time 2021-07-21 23:51
 * @Description 编写一个通用的动态代理实现的类！所有的代理对象设置为Object即可！
 */
public class ProxyInvocationHandlerCommon implements InvocationHandler {

    private ProxyLog proxyLog;
    private Object target;

    // 生成代理类
    public void setTarget(Object target){
        this.target = target;
    }

    // proxy：代理类
    // method：代理类的调用处理程序的方法对象
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable{
        proxyLog.log_proxy(method.getName());
        Object result = method.invoke(target, args);
        return result;
    }

    public void setProxyLog(String name){
        System.out.println("记录日志方法" + name + "日志");
    }
}
