package static_proxy;

/**
 * @Author sf
 * @File UserService
 * @Time 2021-03-31 20:31
 * @Description
 */
// 1、创建一个抽象角色，比如咋们平时做的用户业务，抽象起来就是增删改查！
//      抽象角色：增删改查业务
public interface UserService {
	
	void adds();
	void delete();
	void update();
	void query();
}
