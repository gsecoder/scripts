package ioc_create_object;

/**
 * @Author secoder
 * @File UserT
 * @Time 2021-03-24 21:29
 * @Description
 */
public class UserT {
	
	private String name;
	
	// 有参构造器
	public UserT(String name){
		this.name = name;
	}
	
	public void setName(String name){
		this.name = name;
	}
	
	public void show(){
		System.out.println("name = " + name);
	}
}
