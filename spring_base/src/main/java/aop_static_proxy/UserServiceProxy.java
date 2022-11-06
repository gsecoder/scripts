package aop_static_proxy;

/**
 * @Author secoder
 * @File UserServiceProxy
 * @Time 2021-07-21 20:26
 * @Description
 */
public class UserServiceProxy implements UserService{
	
	private UserServiceImpl userServiceImpl;
	private ProxyLog proxyLog;
	
	public void setUserService(UserServiceImpl userServiceImpl){
		this.userServiceImpl = userServiceImpl;
	}
	
	@Override
	public void add() {
		proxyLog.log_proxy("add");
		userServiceImpl.add();
	}
	
	@Override
	public void delete() {
		proxyLog.log_proxy("delete");
		userServiceImpl.delete();
	}
	
	@Override
	public void update(){
		proxyLog.log_proxy("update");
		userServiceImpl.update();
	}
	
	@Override
	public void query(){
		proxyLog.log_proxy("query");
		userServiceImpl.query();
	}
}
