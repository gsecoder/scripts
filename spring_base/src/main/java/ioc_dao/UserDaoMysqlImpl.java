package ioc_dao;

/**
 * 新增一个UserDao接口的UserDaoMysql实现类
 */
public class UserDaoMysqlImpl implements UserDao{
	@Override
	public void getUser() {
		System.out.println("通过MySQL获取用户数据");
	}
}
