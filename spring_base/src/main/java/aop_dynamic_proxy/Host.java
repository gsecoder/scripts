package aop_dynamic_proxy;

/**
 * @Author secoder
 * @File Host
 * @Time 2021-07-21 23:20
 * @Description 真实角色：房东，房东要出租房子
 */
public class Host implements Rent{

    public void rent(){
        System.out.println("房东Host出租房子");
    }
}
