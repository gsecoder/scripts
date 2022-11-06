package com.secode.spring_boot.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @Author secoder
 * @File Employee
 * @Time 2021-07-13 22:54
 * @Description
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Employee {

    private String name;
    private String email;
    private Boolean gender;
    private String department;

}
