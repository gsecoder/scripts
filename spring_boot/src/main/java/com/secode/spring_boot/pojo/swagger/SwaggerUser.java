package com.secode.spring_boot.pojo.swagger;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.annotations.ApiOperation;

/**
 * @Author secoder
 * @File SwaggerUser
 * @Time 2021-07-15 14:50
 * @Description
 */
@Api(tags = "作用在类上的模块说明")
@ApiModel("用户实体类")
public class SwaggerUser {
	@ApiModelProperty("用户名")
	public String username;
	@ApiModelProperty("密码")
	public String password;
	
	@ApiOperation("作用在方法上，获取用户名")
	public String getUsername() {
		return username;
	}
	
	public void setUsername(String username) {
		this.username = username;
	}
	
	public String getPassword() {
		return password;
	}
	
	public void setPassword(String password) {
		this.password = password;
	}
}
