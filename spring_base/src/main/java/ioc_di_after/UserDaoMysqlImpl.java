package ioc_di_after;

/**
 * @Author secoder
 * @File UserDaoMysqlImpl
 * @Time 2021-07-19 20:28
 * @Description
 */
public class UserDaoMysqlImpl implements UserDao{
	
	@Override
	public void getUser(){
		System.out.println("Dao Mysql获取数据");
	}
}
