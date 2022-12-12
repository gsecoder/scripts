package base;

/**
 * @file base.MethodParTransmit
 * @author sf
 * @date 2020/8/18 8:10 下午
 * @description 值传递和引用传递
 */

public class MethodParTransmit {

public static void main(String[] args) {
	// 引用传递:对象，本质还是值传递
	Student student = new Student();
	System.out.println(student.name);
	MethodParTransmit.change(student);
	System.out.println(student.name);
	
	
	// 值传递
	int a = 1;
	System.out.println(a);
	changeA(a);
	System.out.println(a);
	
}

public static void change(Student student) {
	// student 是一个具体的对象，可以更改属性
	student.name = "新名字";
}

public static void changeA(int a) {
	a = 10;
}
}

class Student {
String name;
}