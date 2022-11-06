/**
 * @file AnnotationReflexAnnotation
 * @author sf
 * @date 2020/8/28 8:59 下午
 * @description 注解
 */

import java.lang.annotation.*;

public class AnnotationReflexAnnotation {

public static void main(String[] args) {
	// main 方法
	
	// 注解可以显示赋值，如果没有默认值，我们就必须给注解赋值
//		@MyAnnotation1(age = 18, name = "crisimple")
	
	
}
}

class MyAnnotation {
// 注解可以显示赋值，如果没有默认值，我们就必须给注解赋值
@MyAnnotation1(age = 18, name = "crisimple")
public void test1() {
	
}

@MyAnnotation2(name = "测试")
public void test2() {
	
}
	
	
}


/**
 * 自定义注解
 */
// @Target 表示我们的注释可以用在哪些地方
@Target({ElementType.TYPE, ElementType.METHOD})
// @Retention 表示我们的注解在什么地方还有效
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnnotation1 {
// 注解的参数：参数类型 + 参数名()
String name() default "";

int age();

// 如果默认为 -1，代表不存在
int id() default -1;

String[] schools() default {"大学", "高中"};
}

@Target({ElementType.TYPE, ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnnotation2 {
// 如果只有一个的时候，不要写名字默认就是 value
String name();
}

