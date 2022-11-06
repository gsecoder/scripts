package com.secode.spring_boot.controller.mybatis;

import com.secode.spring_boot.mapper.DepartmentMapper;
import com.secode.spring_boot.pojo.Department;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * @Author secoder
 * @File DepartmentController
 * @Time 2021-07-13 21:23
 * @Description
 */

@RestController
@RequestMapping("jdbc")
public class DepartmentController {
	
	@Autowired
	DepartmentMapper departmentMapper;
	
	/**
	 * 查询全部部门
	 * @return
	 */
	@GetMapping("/getDepartments")
	public List<Department> getDepartments(){
		return departmentMapper.getDepartments();
	}
	
	/**
	 * 根据ID查询部门信息
	 */
	@GetMapping("/getDepartment/{id}")
	public Department getDepartment(@PathVariable("id") String id){
		return departmentMapper.getDepartment(id);
	}
}
