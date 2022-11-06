package com.secode.spring_boot.controller.mybatis;

import com.secode.spring_boot.mapper.EmployeeMapper;
import com.secode.spring_boot.pojo.Employee;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * @Author secoder
 * @File EmployeeController
 * @Time 2021-07-13 23:45
 * @Description
 */
@RestController
@RequestMapping("jdbc")
public class EmployeeController {

    @Autowired
    EmployeeMapper employeeMapper;

    /**
     * 查询全员信息
     */
    @GetMapping("/getEmployees")
    public List<Employee> getEmployees(){
        return employeeMapper.getEmployees();
    }

    /**
     * 根据员工名字查询员工信息
     */
    @GetMapping("/getEmployee/{name}")
    public List<Employee> getEmployee(@PathVariable("name") String name){
        return employeeMapper.getEmployee(name);
    }

    /**
     * 新增一个员工
     */
    @PostMapping("/saveEmployee")
    public String saveEmployee(){
        Employee employee = new Employee();
        employee.setName("员工A");
        employee.setEmail("a@qq.com");
        employee.setGender(true);
        employee.setDepartment("部门1");
        return employeeMapper.saveEmployee(employee);
    }

    /**
     * 删除员工
     */
    @PostMapping("/deleteEmployee/{name}")
    public String deleteEmployee(@PathVariable("name") String name){
        return employeeMapper.deleteEmployee(name);
    }
}
