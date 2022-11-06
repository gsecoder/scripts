package ioc_annotation;

/**
 * @Author secoder
 * @File Dog
 * @Time 2021-03-27 20:19
 * @Description
 */
public class Dog {
	
	private String name;

	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public void shout(){
		System.out.println("wang~~");
	}
}
