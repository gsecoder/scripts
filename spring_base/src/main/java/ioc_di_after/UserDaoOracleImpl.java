package ioc_di_after;

/**
 * @Author secoder
 * @File UserDaoOracleImpl
 * @Time 2021-07-19 20:29
 * @Description
 */
public class UserDaoOracleImpl implements UserDao{
	
	@Override
	public void getUser(){
		System.out.println("UserDao Oracle获取数据");
	}
}
