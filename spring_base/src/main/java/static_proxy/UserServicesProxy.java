package static_proxy;

/**
 * @Author sf
 * @File UserServiceProxy
 * @Time 2021-03-31 20:38
 * @Description
 * 3、需求来了，现在我们需要增加一个日志功能，怎么实现！
 *      思路1 ：在实现类上增加代码 【麻烦！】
 *      思路2：使用代理来做，能够不改变原来的业务情况下，实现此功能就是最好的了！
 * 4、设置一个代理类来处理日志！代理角色
 *      
 */
public class UserServicesProxy implements UserService {
	
	// 代理角色，在这里面增加日志的实现
	private UserServiceImpl userService;
	
	public void setUserServiceImpl(UserServiceImpl userService){
		this.userService = userService;
	}

	@Override
	public void adds() {
		log("add");
		userService.adds();
	}

	public void delete() {
		log("delete");
		userService.delete();
	}
	
	public void update() {
		log("update");
		userService.update();
	}
	
	public void query() {
		log("query");
		userService.query();
	}
	
	public void log(String msg){
		System.out.println("执行了" + msg + "方法");
	}
}
