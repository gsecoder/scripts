package ioc_auto_assembly;

/**
 * @Author sf
 * @File User
 * @Time 2021-03-27 20:25
 * @Description
 */
public class User {
	
	private Cat cat;
	private Dog dog;
	private String str;

	public Cat getCat() {
		return cat;
	}
	
	public void setCat(Cat cat) {
		this.cat = cat;
	}
	
	public Dog getDog() {
		return dog;
	}
	
	public void setDog(Dog dog) {
		this.dog = dog;
	}
	
	public String getStr() {
		return str;
	}
	
	public void setStr(String str) {
		this.str = str;
	}
}
