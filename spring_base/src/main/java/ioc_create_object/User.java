package ioc_create_object;

/**
 * @Author sf
 * @File User
 * @Time 2021-03-24 21:14
 * @Description
 */
public class User {
	
	private String name;
	
	// 无参构造器
	public User(){
		System.out.println("User的无参构造方法1");
	}
	
	public void setName(String name){
		this.name = name;
	}
	
	public void show(){
		System.out.println("show() name = " + name);
	}
}
