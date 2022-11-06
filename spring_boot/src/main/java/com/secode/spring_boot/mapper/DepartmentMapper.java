package com.secode.spring_boot.mapper;

import com.secode.spring_boot.pojo.Department;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * @Author secoder
 * @File DepartmentMapper
 * @Time 2021-07-12 23:37
 * @Description DepartmentMapper
 */

// @Mapper : 表示本类是一个 MyBatis 的 Mapper
@Mapper
@Repository
public interface DepartmentMapper {

    /**
     * 获取所有部门信息
     */
    List<Department> getDepartments();

    /**
     * 通过id获取部门
     */
    Department getDepartment(String id);
}
