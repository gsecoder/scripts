/**
 * @file OOPMethodCall
 * @author sf
 * @date 2020/8/18 7:29 下午
 * @description 方法的调用
 */

public class OopMethodCall {

public static void main(String[] args) {
	// main 方法
	/**
	 * 静态方法直接通过 类.静态方法名，来调用
	 */
	Personx Personx = new Personx();
	Personx.say();
	
	/**
	 * 通过实例化对象，实例化对象.非静态方法名
	 */
	Animal animal = new Animal();
	animal.asay();
	
}
}

class Personx {
/**
 * 静态方法
 */
public static void say() {
	System.out.println("人说话了......");
}
}


class Animal {
/**
 * 非静态方法
 */
public void asay() {
	System.out.println("动物在叫");
}
}