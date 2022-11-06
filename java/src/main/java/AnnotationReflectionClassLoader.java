/**
 * @file AnnotationReflectionClassLoader
 * @author sf
 * @date 2020/9/1 2:41 下午
 * @description 类加载器的作用
 */

public class AnnotationReflectionClassLoader {

public static void main(String[] args) throws ClassNotFoundException {
	// main 方法
	
	// 1、获取系统类的加载器
	ClassLoader systemClassLoader = ClassLoader.getSystemClassLoader();
	System.out.println(systemClassLoader);
	
	// 2、获取系统类加载器的父类加载器 ---> 扩展类加载器
	ClassLoader parent = systemClassLoader.getParent();
	System.out.println(parent);
	
	// 3、获取扩展类加载器的父类加载器 ---> 根加载器（c/c++）
	ClassLoader parent1 = parent.getParent();
	// 因为是 c/c++ 写的，所以无法直接获取到
	System.out.println(parent1);
	
	// 4、测试当前类是那个加载器加载的
	ClassLoader classLoader = Class.forName("com.java.base.AnnotationReflectionClassLoader").getClassLoader();
	System.out.println(classLoader);
	
	// 5、测试 JDK 内置的类是谁加载的
	ClassLoader classLoader1 = Class.forName("java.lang.Object").getClassLoader();
	System.out.println(classLoader1);
	
	// 6、获取系统类加载器可以加载路径
	System.out.println(System.getProperty("java.class.path"));
	
	// 7、双亲委派机制：自定义和系统类相同的类，比如：java.lang.String，系统会自己找到系统的不会去找自定义的
}
}

class TempAnnotationReflectionClassLoader {
// 空类
}
