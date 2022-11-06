package com.secode.spring_boot.controller.swagger;

import com.secode.spring_boot.pojo.swagger.SwaggerUser;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

/**
 * @Author secoder
 * @File SwaggerUserController
 * @Time 2021-07-15 15:02
 * @Description
 */
@RestController
public class SwaggerUserController {
	
	@ApiOperation("获取Swagger用户的接口")
	@GetMapping("/getSwaggerUser")
	@ResponseBody
	public SwaggerUser getSwaggerUser(){
		return new SwaggerUser();
	}
	
	@ApiOperation("通过username获取Swagger用户的接口")
	@PostMapping("/getSwaggerUserByName")
	@ResponseBody
	public String getSwaggerUserByName(@ApiParam("这个名字会被返回") String username){
		return username;
	}
}
