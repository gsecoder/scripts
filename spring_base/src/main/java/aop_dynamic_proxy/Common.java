package aop_dynamic_proxy;

/**
 * @Author secoder
 * @File Common
 * @Time 2021-07-22 00:03
 * @Description 其实这是个测试类
 */
public class Common {

    public static void main(String[] args) {

        // 真实对象
        UserServiceImpl userServiceImpl = new UserServiceImpl();

        // 代理对象的调用处理程序
        ProxyInvocationHandler proxyInvocationHandler = new ProxyInvocationHandler();
        proxyInvocationHandler.setTarget(userServiceImpl);
        // 动态生成代理类
        UserService proxy = (UserService) proxyInvocationHandler.getProxy();
        proxy.add();
    }
}
