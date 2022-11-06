package ioc_annotation;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

/**
 * @Author secoder
 * @File Person
 * @Time 2021-03-30 19:46
 * @Description
 */
// 2、在指定包下编写类，增加注解；相当于配置文件中 <bean id="user" class="当前注解的类"/>
@Component("person")
public class Person {
	
	public String name = "person...";
	
	@Value("27")
	// 相当于配置文件中 <property name="age" value="27"/>
	public int age;
	
	public boolean sex;

	public int getAge() {
		return age;
	}

	public boolean getSex() {
		return sex;
	}
	
	@Value("true")
	public void setSex(boolean sex) {
		this.sex = sex;
	}
}
