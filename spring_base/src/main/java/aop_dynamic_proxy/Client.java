package aop_dynamic_proxy;

/**
 * @Author secoder
 * @File Client
 * @Time 2021-07-21 23:34
 * @Description 租客
 */
public class Client {

    // 核心：一个动态代理 , 一般代理某一类业务 , 一个动态代理可以代理多个类，代理的是接口！
    public static void main(String[] args) {
        // 真实角色
        Host host = new Host();

        // 代理实例的调用处理程序
        ProxyInvocationHandler proxyInvocationHandler = new ProxyInvocationHandler();
        // 将真实角色放置进去
        proxyInvocationHandler.setRent(host);
        // 动态生成对应的代理类！
        Rent proxy = (Rent) proxyInvocationHandler.getProxy();
        proxy.rent();
    }
}
