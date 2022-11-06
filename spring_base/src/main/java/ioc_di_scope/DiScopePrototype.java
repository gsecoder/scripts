package ioc_di_scope;

/**
 * @Author sf
 * @File DiScopePrototype
 * @Time 2021-03-27 19:13
 * @Description
 */
public class DiScopePrototype {
	
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
