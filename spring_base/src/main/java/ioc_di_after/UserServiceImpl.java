package ioc_di_after;

/**
 * @Author secoder
 * @File UserServiceImpl
 * @Time 2021-07-19 19:37
 * @Description
 */
public class UserServiceImpl implements UserService{
	
	//private UserDao userDao = new UserDaoImpl();
	// 可以在需要用到他的地方 , 不去实现它 , 而是留出一个接口 , 利用set , 我们去代码里修改下
	private UserDao userDao;
	public void setUserDao(UserDao userDao){
		this.userDao = userDao;
	}
	
	@Override
	public void getUser(){
		userDao.getUser();
	}
}
