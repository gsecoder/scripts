package com.secode.spring_boot.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

/**
 * @Author secoder
 * @File JDBCController
 * @Time 2021-07-12 15:59
 * @Description
 */
@RestController
@RequestMapping("jdbc")
public class JDBCController {

	/**
	 * SpringBoot 默认提供了数据源，默认提供了org.springframework.jdbc.core.JdbcTemplate
	 * JdbcTemplate 中会自己注入数据源，用于简化 JDBC操作，还能避免一些常见的错误,使用起来也不用再自己来关闭数据库连接
	 */
	@Autowired
	JdbcTemplate jdbcTemplate;
	
	/**
	 * 【查】查询employee表中查询
	 * 		List 中的1个 Map 对应数据库的 1行数据
	 * 		Map 中的 key 对应数据库的字段名，value 对应数据库的字段值
	 */
	@GetMapping("/userList")
	public List<Map<String, Object>> userList(){
		String sql = "SELECT * FROM employee";
		List<Map<String, Object>> maps = jdbcTemplate.queryForList(sql);
		return maps;
	}
	
	/**
	 * 【增】新增用户
	 */
	@PostMapping("/userAdd")
	public String addUser(){
		// 插入语句
		String sql = "INSERT INTO employee(name, email,gender,department)" +
					 "VALUES ('B', 'b@163.com', 0, 102)";
		
		jdbcTemplate.update(sql);
		
		// 添加成功
		return "addOk";
	}
	
	/**
	 * 【改】修改用户信息
	 */
	@PostMapping("/userUpdate/{name}")
	public String updateUser(@PathVariable("name") String name){
		// 插入语句
		String sql = "update employee set email=? where name=" + name;
		
		// 数据
		Object[] objects = new Object[1];
		objects[0] = "a@163.com";
		jdbcTemplate.update(sql, objects);
		
		// 更新成功
		return "updateOk";
	}
	
	/**
	 * 删除用户
	 */
	@DeleteMapping("/userDelete/{name}")
	public String deleteUser(@PathVariable("name") String name){
		// 删除语句
		String sql = "DELETE FROM employee WHERE name = ?";
		jdbcTemplate.update(sql, name);
		
		// 删除成功
		return "deleteOk";
	}
}
