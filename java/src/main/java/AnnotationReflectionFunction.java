/**
 * @file AnnotationReflexReflection
 * @author sf
 * @date 2020/8/31 4:03 下午
 * @description 反射机制
 */

public class AnnotationReflectionFunction {

public static void main(String[] args) {
	// main 方法
	
	// 1. 通过反射获取类的 class 对象
	try {
		Class c1 = Class.forName("com.java.base.AnnotationReflectionFunction");
		System.out.println(c1);
		
		// 2. 获取到对象后我们就可以获取到对象的属性、方法等
		// c1.
		
		// 3.一个类只有一个 Class 类对象
		//   一个类被加载后，类的整个结构都会被封装在 Class 对象中
		Class c2 = Class.forName("com.java.base.AnnotationReflectionFunction");
		Class c3 = Class.forName("com.java.base.AnnotationReflectionFunction");
		Class c4 = Class.forName("com.java.base.AnnotationReflectionFunction");
		System.out.println(c2.hashCode());
		System.out.println(c3.hashCode());
		System.out.println(c4.hashCode());
	} catch (ClassNotFoundException e) {
		e.printStackTrace();
	}
}
}


/**
 * 实体类：就是一个拥有Set和Get方法的类
 */
class ReflectionClass {
private String name;
private int id;
private int age;

public ReflectionClass() {
	
}

public ReflectionClass(String name, int id, int age) {
	this.name = name;
	this.id = id;
	this.age = age;
}

public String getName() {
	return name;
}

public void setName(String name) {
	this.name = name;
}

public int getId() {
	return id;
}

public void setId(int id) {
	this.id = id;
}

public int getAge() {
	return age;
}

public void setAge(int age) {
	this.age = age;
}
}
