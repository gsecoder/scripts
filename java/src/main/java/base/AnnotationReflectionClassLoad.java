package base;

/**
 * @file base.AnnotationReflectionClassLoad
 * @author sf
 * @date 2020/9/1 12:59 上午
 * @description
 */

public class AnnotationReflectionClassLoad {

public static void main(String[] args) {
	// main 方法
	
	/**
	 * 1、加载到内存，产生一个类对应的 Class 对象
	 * 2、链接，链接结束后 m = 0
	 * 3、初始化
	 *  <clinit>(){
	 *      System.out.println("base.TempA 类静态代码初始化");
	 *      m = 3000;
	 *      m = 1000;
	 *  }
	 *  m = 1000;
	 */
}
}

class TempA {
static {
	System.out.println("base.TempA 类静态代码初始化");
	int m = 3000;
}

static int m = 1000;

public TempA() {
	System.out.println("base.TempA 的无参构造器初始化");
}
}