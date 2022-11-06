package spring_application;

/**
 * @Author secoder
 * @File Hello
 * @Time 2021-03-24 8:13 下午
 * @Description
 */
public class Hello {
	
	private String name;

	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public void show(){
		System.out.println("Hello, " + name);
	}
}

