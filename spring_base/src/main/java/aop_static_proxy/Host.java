package aop_static_proxy;

/**
 * @Author secoder
 * @File Host
 * @Time 2021-07-21 20:03
 * @Description
 */
public class Host implements Rent{
	
	public void rent(){
		System.out.println("房屋出租");
	}
}
