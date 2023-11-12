package com.secode.spring_boot.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.Environment;
import org.springframework.core.env.Profiles;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.Contact;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

import java.util.ArrayList;

/**
 * @Author secoder
 * @File SwaggerConfig
 * @Time 2021-07-14 20:45
 * @Description 配置swagger
 */

@Configuration		// 配置类
@EnableSwagger2		// 开启Swagger2的自动配置
public class SwaggerConfigController {
	
	@Bean
	public Docket docket(Environment environment){
		// 设置要显示的Swagger的环境
		Profiles profiles = Profiles.of("dev", "com.secoder.test");
		// 判断当前是否处于该环境，通过enable()接收此参数是否要显示
		boolean flag = environment.acceptsProfiles(profiles);
		System.out.println("flag: " + flag);
		
		return new Docket(DocumentationType.SWAGGER_2)
					   .apiInfo(apiInfo())
					   // 配置分组
					   .groupName("MyBatis")
					   // 配置是否启用Swagger，如果是false，在浏览器将无法访问
					   .enable(true)	
					   // 通过.select()方法，去配置扫描接口,RequestHandlerSelectors配置如何扫描接口
				       .select()
					   .apis(RequestHandlerSelectors.basePackage("com.secode.spring_boot.controller"))
				       .build();
	}
	@Bean
	public Docket docket2() {
	   return new Docket(DocumentationType.SWAGGER_2)
		  .apiInfo(apiInfo())
		  .select()// 通过.select()方法，去配置扫描接口,RequestHandlerSelectors配置如何扫描接口
		  .apis(RequestHandlerSelectors.basePackage("com.secode.spring_boot.controller"))
		   // 配置如何通过path过滤，即这里只扫描请求以/jdbc/开头的接口
		  .paths(PathSelectors.ant("/jdbc/**"))
		  .build();
	}
	
	// 配置文档信息
	private ApiInfo apiInfo(){
		Contact contact = new Contact(
				"secoder",
				"https://www.github.com/iscoder",
				"crisimple@qq.com"
		);
		
		return new ApiInfo(
				"SpringBoot集成Swagger",	// Swagger的标题
				"Swagger如何配置",	// Swagger的描述信息
				"V1.0",		// Swagger的版本信息
				"https://www.github.com/iscoder", 	// 组织信息
				contact,
				"Apache 2.0许可",		// 开源许可
				"许可链接",
				new ArrayList<>()	// 扩展
		);
	}
}
