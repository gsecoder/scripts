package static_proxy;

/**
 * @Author sf
 * @File LandordProxy
 * @Time 2021-03-31 17:59
 * @Description LandordProxy.java 房屋中介
 */
public class LandordProxy implements Landlord{
	
	private LandlordA landlordA;
	
	public LandordProxy(){
	}
	
	public LandordProxy(LandlordA landlordA){
		this.landlordA = landlordA;
	}
	
	public void rent(){
		seeHouse();
		landlordA.rent();
		fee();
	}
	
	public void seeHouse(){
		System.out.println("带房客看房");
	}
	
	public void fee(){
		System.out.println("收中介费");
	}
}
