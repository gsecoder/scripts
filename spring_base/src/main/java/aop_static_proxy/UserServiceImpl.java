package aop_static_proxy;

/**
 * @Author secoder
 * @File UserServiceImpl
 * @Time 2021-07-21 20:21
 * @Description
 */
public class UserServiceImpl implements UserService{
	
	@Override
	public void add() {
		System.out.println("add() 增加了一个用户");
	}
	
	@Override
	public void delete() {
		System.out.println("delete() 删除了一个用户");
	}
	
	@Override
	public void update() {
		System.out.println("update() 更新了一个用户");
	}
	
	@Override
	public void query() {
		System.out.println("query() 查询了一个用户");
	}
}
