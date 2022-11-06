package com.secode.spring_boot.pojo;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;
import org.springframework.validation.annotation.Validated;

import javax.validation.constraints.AssertTrue;
import javax.validation.constraints.Email;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Null;
import java.util.Date;
import java.util.List;
import java.util.Map;

/**
 * @Author secoder
 * @File Person
 * @Time 2021-07-11 22:59
 * @Description
 */

@Component  // 注册bean
// https://docs.spring.io/spring-boot/docs/2.4.5/reference/html/appendix-configuration-metadata.html#configuration-metadata-annotation-processor
@ConfigurationProperties(prefix = "person")
@Validated  // 数据校验
public class Person {

    /**
     * 空检查
     *  @Null 验证对象是否为null
     *  @NotNull 验证对象是否不为null, 无法查检长度为0的字符串
     *  @NotBlank 检查约束字符串是不是Null还有被Trim的长度是否大于0, 只对字符串, 且会去掉前后空格.
     *  @NotEmpty 检查约束元素是否为NULL或者是EMPTY.
     */
    @NotNull(message = "名字不能为空")
    private String name;
    private Integer age;
    /**
     * Boolean 检查
     *  @AssertTrue 验证 Boolean 对象是否为 true
     *  @AssertFalse 验证 Boolean 对象是否为 false
     */
    @AssertTrue(message = "状态不能为是否为true")
    private Boolean happy;
    /**
     * 日期检查
     *  @Past 验证 Date 和 Calendar 对象是否在当前时间之前
     *  @Future 验证 Date 和 Calendar 对象是否在当前时间之后
     *  @Pattern 验证 String 对象是否符合正则表达式的规则
     */
    private Date birthday;
    @Email(message = "邮箱格式错误")
    private String email;
    private Map<String, Object> maps;
    /**
     * 长度检查
     *  @Size(min=, max=) 验证对象（Array,Collection,Map,String）长度是否在给定的范围之内
     *  @Length(min=, max=) string is between min and max included.
     */
    private List<Object> lists;
    @Null(message = "验证对象是否为null")
    private Dog dog;

    public Person() {
    }

    public Person(String name, Integer age, Boolean happy, Date birthday, String email, Map<String, Object> maps, List<Object> lists, Dog dog) {
        this.name = name;
        this.age = age;
        this.happy = happy;
        this.birthday = birthday;
        this.email = email;
        this.maps = maps;
        this.lists = lists;
        this.dog = dog;
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

    public Boolean getHappy() {
        return happy;
    }

    public void setHappy(Boolean happy) {
        this.happy = happy;
    }

    public Date getBirthday() {
        return birthday;
    }

    public void setBirthday(Date birthday) {
        this.birthday = birthday;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Map<String, Object> getMaps() {
        return maps;
    }

    public void setMaps(Map<String, Object> maps) {
        this.maps = maps;
    }

    public List<Object> getLists() {
        return lists;
    }

    public void setLists(List<Object> lists) {
        this.lists = lists;
    }

    public Dog getDog() {
        return dog;
    }

    public void setDog(Dog dog) {
        this.dog = dog;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", happy=" + happy +
                ", birthday=" + birthday +
                ", email='" + email + '\'' +
                ", maps=" + maps +
                ", lists=" + lists +
                ", dog=" + dog +
                '}';
    }
}
