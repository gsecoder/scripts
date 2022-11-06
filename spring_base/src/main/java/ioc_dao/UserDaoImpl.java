package ioc_dao;

/**
 * UserDao接口的实现类
 */
public class UserDaoImpl implements UserDao{
	@Override
	public void getUser(){
		System.out.println("UserDao获取用户数据");
	}
}
