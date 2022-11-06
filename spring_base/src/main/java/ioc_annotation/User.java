package ioc_annotation;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import javax.annotation.Resource;

/**
 * @Author secoder
 * @File User
 * @Time 2021-03-29 21:41
 * @Description
 */
// 2、在指定包下编写类，增加注解, 相当于配置文件中 <bean id="user" class="当前注解的类"/>
@Component("user")
public class User {
	
	// @Autowired(required=false)  说明：false，对象可以为null；true，对象必须存对象，不能为null。
	@Autowired
	@Qualifier(value = "cat")
	private Cat cat;
	
	@Resource
	private Dog dog;
	
	public String name="user_name";
	
	// 属性注入， 可以不用提供set方法，直接在直接名上添加@value("值")
	// 如果提供了set方法，在set方法上添加@value("值");
	@Value("12")
	public int age;
	
	private String str;
	
	public void setName(String name) {
		this.name = name;
	}

	public Cat getCat() {
		return cat;
	}
	
	public Dog getDog() {
		return dog;
	}
	
	public String getStr() {
		return str;
	}
	
	@Value("Set设置的str的名字")
	public void setStr(String str){
		this.str = str;
	}

	@Override
	public String toString() {
		return "User{" +
				       "dog=" + dog +
				       '}';
	}
}
