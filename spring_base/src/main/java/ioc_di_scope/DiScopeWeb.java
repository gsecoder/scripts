package ioc_di_scope;

/**
 * @Author sf
 * @File DiScopeWeb
 * @Time 2021-03-27 19:35
 * @Description
 */
public class DiScopeWeb {
	
	private String name;

	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}

	@Override
	public String toString() {
		return "la......" + name;
	}
}
