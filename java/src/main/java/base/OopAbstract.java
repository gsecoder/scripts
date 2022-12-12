package base;

/**
 * @file base.OopAbstract
 * @author sf
 * @date 2020/8/21 2:41 下午
 * @description 抽象类、抽象方法
 */

public class OopAbstract {

public static void main(String[] args) {
	// main 方法
	/**
	 * 抽象类不能用new关键字来创建对象
	 * 但是：可以在继承了抽象类的子类中通过super()或super(参数列表)调用抽象类中的构造方法
	 */
//        new base.Father(); 报错
	Child child1 = new Child(9);
	System.out.println(child1);
	
	
}
}

/**
 * 父类抽象类
 */
abstract class Father {

/**
 * 抽象类是有构造器的，只是不能创建抽象类的实例对象
 */
public Father(int par) {
	System.out.println("抽象父类有参构造器传参值为：" + par);
}

/**
 * 抽象方法必须存在于抽象类中
 * 抽象方法的存在就是定义标准，
 * 抽象方法可以只有方法名称，没有实现方法的实现。
 */
public abstract void abstractFatherMethod();
	
}

class Child extends Father {
public Child(int par) {
	super(par);
	System.out.println("抽象子类的有参构造器传参值为：" + par);
}

/**
 * 子类必须重写父类的抽象方法，否则子类也得被定义为抽象子类（IDEA编辑器中的表现形式就是报错）
 */
@Override
public void abstractFatherMethod() {
	System.out.println("这是子类重新的父类的抽象方法");
}
}