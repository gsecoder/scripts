package aop_realization_three.custom_class_aop;

/**
 * @Author secoder
 * @File CustomAop
 * @Time 2021-07-22 17:17
 * @Description
 */
public class DiyPointcut {
	
	public void before(){
		System.out.println("----- 方法前执行 -----");
	}
	
	public void after(){
		System.out.println("----- 方法后执行 -----");
	}
}
