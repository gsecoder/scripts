package aop_realization_three.custom_class_aop;

/**
 * @Author secoder
 * @File UserServiceImpl
 * @Time 2021-07-22 17:16
 * @Description
 */
public class UserServiceImpl implements UserService{
	
	@Override
	public void add() {
		System.out.println("add() 新增用户");
	}
	
	@Override
	public void query() {
		System.out.println("query() 查询用户");
	}
}
