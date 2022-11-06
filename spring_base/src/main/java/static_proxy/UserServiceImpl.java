package static_proxy;

/**
 * @Author sf
 * @File UserServiceImpl
 * @Time 2021-03-31 20:34
 * @Description
 */
// 2、我们需要一个真实对象来完成这些增删改查操作
//      真实对象，完成增删改查操作的人
public class UserServiceImpl implements UserService {
	
	public void adds(){
		System.out.println("增加用户");
	}
	
	public void delete(){
		System.out.println("删除用户");
	}
	
	public void update(){
		System.out.println("更新用户");
	}
	
	public void query(){
		System.out.println("查询用户");
	}
}
