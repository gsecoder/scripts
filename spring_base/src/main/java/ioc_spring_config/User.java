package ioc_spring_config;

/**
 * @Author secoder
 * @File User
 * @Time 2021-07-20 20:33
 * @Description
 */
public class User {
	
	private String username;
	
	// 无参构造器
	public User(){
		System.out.println("User的无参构造器");
	}
	
	public void setUsername(String username) {
		this.username = username;
	}
	
	public void show(){
		System.out.println("UserClass中的show() username=" + username);
	}
}
