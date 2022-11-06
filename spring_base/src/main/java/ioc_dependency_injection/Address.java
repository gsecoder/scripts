package ioc_dependency_injection;

/**
 * @Author sf
 * @File Address
 * @Time 2021-03-26 20:50
 * @Description
 */
public class Address {
	
	private String address;
	
	public String getAddress(){
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	@Override
	public String toString() {
//		return "Address{" +
//				       "address='" + address + '\'' +
//				       '}';
		return address;
	}
}
