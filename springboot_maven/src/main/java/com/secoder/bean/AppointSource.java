package com.secoder.bean;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.PropertySource;
import org.springframework.stereotype.Component;

/**
 * \@PropertySource 指定读取配置文件
 * \@ConfigurationProperties报红，引入此依赖；导入这个包后，后面编写配置时就有提示了
 */
@PropertySource(value = {"classpath:properties/appointSource.properties"})
@Component
@EnableConfigurationProperties(AppointSource.class)
@ConfigurationProperties(prefix = "appoint-source")
public class AppointSource {
	
	public String appointSourceName;
	public Integer age;
	public Boolean sex;
	
	@Override
	public String toString() {
		return "AppointSource{" +
					   "appointSourceName='" + appointSourceName + '\'' +
					   ", age=" + age +
					   ", sex=" + sex +
					   '}';
	}
	
	public String getAppointSourceName() {
		return appointSourceName;
	}
	public void setAppointSourceName(String appointSourceName) {
		this.appointSourceName = appointSourceName;
	}
	
	public Integer getAge() {
		return age;
	}
	public void setAge(Integer age) {
		this.age = age;
	}
	
	public Boolean getSex() {
		return sex;
	}
	public void setSex(Boolean sex) {
		this.sex = sex;
	}
}
