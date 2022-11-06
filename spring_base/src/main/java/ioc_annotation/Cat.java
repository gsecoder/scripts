package ioc_annotation;

/**
 * @Author secoder
 * @File Cat
 * @Time 2021-03-27 20:15
 * @Description
 */
public class Cat {

	private String name;

	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}

	public void shout(){
		System.out.println("miao~~~");
	}
}
