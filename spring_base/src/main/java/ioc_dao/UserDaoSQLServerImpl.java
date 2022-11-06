package ioc_dao;

/**
 * 新增一个UserDao接口的UserDaoSQLServer实现类
 */
public class UserDaoSQLServerImpl implements UserDao{
	@Override
	public void getUser() {
		System.out.println("通过SQLServer获取用户数据");
	}
}
