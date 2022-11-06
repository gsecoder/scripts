package ioc_di_scope;

/**
 * @Author sf
 * @File DiScope
 * @Time 2021-03-27 18:36
 * @Description
 */
public class DiScopeSingleton {
	
	private String name;

	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}

	@Override
	public String toString() {
		return name;
	}
}
