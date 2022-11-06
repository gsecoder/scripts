package aop_realization_three.spring_api;

/**
 * @Author secoder
 * @File UserServiceImpl
 * @Time 2021-07-22 15:24
 * @Description
 */
public class UserServiceImpl implements UserService{
	
	@Override
	public void add() {
		System.out.println("add() 增加用户");
	}
	
	@Override
	public void delete() {
		System.out.println("delete() 删除用户");
	}
	
	@Override
	public void update() {
		System.out.println("update() 更新用户");
	}
	
	@Override
	public void query() {
		System.out.println("query() 查询用户");
	}
}
