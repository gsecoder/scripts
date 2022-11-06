package com.secode.spring_boot.pojo;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

/**
 * @Author secoder
 * @File Dog
 * @Time 2021-07-11 23:07
 * @Description
 */

@Component  // 注册bean
public class Dog {

    // Dog的属性，注意这里的如果是静态属性的话是不可以赋值的，需要在set方法处赋值
    @Value("大黄")
    private String name;
    @Value("23")
    private Integer age;

    public Dog() {
    }

    public Dog(String name, Integer age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Dog{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
