/**
 * @file Friend
 * @author sf
 * @date 2022/6/12 14:45
 * @description
 */

package com.secoder.bean;

import com.sun.istack.internal.NotNull;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.PropertySource;
import org.springframework.stereotype.Component;
import org.springframework.validation.annotation.Validated;

//@PropertySource(value = {"classpath:properties/friend.properties"})
@Component
//@ConfigurationProperties(prefix = "friend")
@Validated
public class AtValue {
	
	/**
	 * <bean class="Friend">
	 *     <property name="name" value="字面量/${key}从环境变量、配置文件中获取值/#{SpEl}">
	 *     </property>
	 * <bean/>
	 */
	@NotNull
	public String name;
	@Value("#{11*2}")
	public Integer age;
	@Value("true")
	public Boolean girl;
	@Value("test@qq.com")
	public String email;
	
	@Override
	public String toString() {
		return "Friend{" +
					   "name='" + name + '\'' +
					   ", age=" + age +
					   ", girl=" + girl +
					   ", email='" + email + '\'' +
					   '}';
	}
	
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	
	public Integer getAge() {
		return age;
	}
	public void setAge(Integer age) {
		this.age = age;
	}
	
	public Boolean getGirl() {
		return girl;
	}
	public void setGirl(Boolean girl) {
		this.girl = girl;
	}
}
