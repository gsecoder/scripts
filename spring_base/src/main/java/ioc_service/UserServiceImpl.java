package ioc_service;

import ioc_dao.UserDao;

/**
 * UserService的实现类
 */
public class UserServiceImpl implements UserService{

	/**
	 * 这里存在一个问题，如果我们要使用MySQL或SQLServer实现类的话，我们就需要从新去new实现类，得到对象去调用对象getUser()方法
	 *      这里我们的权限控制放在了代码里，通过程序猿去控制；耦合性太高，改一次牵一发而动全身
	 * 
	 * 解决方案：
	 *      我们可以在需要用到他的地方 , 不去实现它 , 而是留出一个接口 , 利用set 
	 */
	// private UserDao userDao = new UserDaoImpl();   修改为下面的代码
	private UserDao userDao;
	
	public void setUserDao(UserDao userDao){
		this.userDao  = userDao;
	}
	
	
	@Override
	public void getUser(){
		userDao.getUser();
	}
}
