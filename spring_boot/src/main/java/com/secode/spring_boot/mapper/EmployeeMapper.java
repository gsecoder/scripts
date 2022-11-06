package com.secode.spring_boot.mapper;

import com.secode.spring_boot.pojo.Employee;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * @Author secoder
 * @File EmployeeMapper
 * @Time 2021-07-13 23:11
 * @Description
 */

@Mapper     // @Mapper : 表示本类是一个 MyBatis 的 Mapper
@Repository
public interface EmployeeMapper {

    /**
     * 获取所有员工的信息
     * @return
     */
    List<Employee> getEmployees();

    /**
     * 通过name获得员工信息
     */
    List<Employee> getEmployee(String name);

    /**
     * 新增一个员工
     */
    String saveEmployee(Employee employee);

    /**
     * 删除一个员工
     */
    String deleteEmployee(String name);
}
