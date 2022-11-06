package ioc_cp_namespace;

/**
 * @Author secoder
 * @File CP
 * @Time 2021-03-29 11:52
 * @Description
 */
public class CP {
	
	private String name;
	private int age;

	public CP(){
	}
	
	public CP(String name) {
	}

	public CP(int age){
	}

	public CP(String name, int age) {
		this.name = name;
		this.age = age;
	}

	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public int getAge() {
		return age;
	}
	
	public void setAge(int age) {
		this.age = age;
	}

	@Override
	public String toString() {
		return "CP{" +
				       "name=" + name + '\'' +
				       ", age=" + age +
				       '}';
	}
}
