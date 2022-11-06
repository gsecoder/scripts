package com.secode.spring_boot.config;

import com.alibaba.druid.pool.DruidDataSource;
import com.alibaba.druid.support.http.StatViewServlet;
import com.alibaba.druid.support.http.WebStatFilter;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.web.servlet.FilterRegistrationBean;
import org.springframework.boot.web.servlet.ServletRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.sql.DataSource;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * @Author secoder
 * @File DruidConfig
 * @Time 2021-07-12 20:15
 * @Description
 */

@Configuration
public class DruidConfig {
	
	/**
	 * 将自定义的Druid数据源添加到容器中，不再让SpringBoot自动创建
	 * 绑定全局配置文件中的druid数据源属性到com.alibaba.druid.pool.DruidDataSource从而让它们生效
	 * 
	 * @ConfigurationProperties(prefix = "spring.datasource")：作用就是将 全局配置文件中
	 * application.yaml前缀为spring.datasource的属性（非默认属性所以需要指定绑定）值注入到 com.alibaba.druid.pool.DruidDataSource 的同名参数中
	 */
	@ConfigurationProperties(prefix = "spring.datasource")
	@Bean
	public DataSource druidDataSource(){
		return new DruidDataSource();
	}
	
	/**
	 * 【Druid后台配置管理】
	 * 【访问地址：http://127.0.0.1:8080/druid/index.html】
	 * 配置Druid监控管理后台的Servlet
	 * 内置Servlet容器时没有web.xml文件，所以使用SpringBoot的注册Servlet方式
	 */
	@Bean
	public ServletRegistrationBean servletRegistrationBean(){
		ServletRegistrationBean servletRegistrationBean = new ServletRegistrationBean(new StatViewServlet(), "/druid/*");
		
		// 这些参数可以在 com.alibaba.druid.support.http.StatViewServlet的父类 com.alibaba.druid.support.http.ResourceServlet 中找到
		Map<String, String> initParams = new HashMap<>();
		// 后台管理界面的登录账号
		initParams.put("loginUsername", "root");
		// 后台管理界面的登录密码
		initParams.put("loginPassword", "Root@159357");
		
		// 后台允许谁可以方法
		// initParams.put("allow", "localhost")：表示只有本机可以访问
		// initParams.put("allow", "")：为空或者为null时，表示允许所有访问
		initParams.put("allow", "");
		
		// 后台拒绝谁可以访问，禁止此IP访问
		//initParams.put("test", "192.168.1.12")
		
		// 设置初始化参数
		servletRegistrationBean.setInitParameters(initParams);
		return servletRegistrationBean;
	}
	
	/**
	 * 【配置Druid web监控filter过滤器】
	 *  WebStatFilter：用于配置Web和Druid数据源之间的管理关联监控统计
	 */
	@Bean
	public FilterRegistrationBean webStatFilter(){
		FilterRegistrationBean bean = new FilterRegistrationBean();
    	bean.setFilter(new WebStatFilter());
    	
    	// exclusions：设置哪些请求进行过滤排除掉，从而不进行统计
		Map<String, String> initParams = new HashMap<>();
		initParams.put("exclusions", "*.js,*.css,/druid/*,/jdbc/*");
		bean.setInitParameters(initParams);
		
		// "/*" 表示过滤所有请求
		bean.setUrlPatterns(Arrays.asList("/*"));
		return bean;
	}
}
