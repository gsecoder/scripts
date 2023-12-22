package com.secoder.java_aipasser.model;

import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Data
@Entity
public class User {

    /*
    * 使用JPA（Java Persistence API）进行对象关系映射（ORM）时，用于标识实体类主键的注解
    * */
    @Id  // @Id 注解用于标识一个实体类的字段作为主键。在数据库表中，对应的字段将会被定义为主。主键的作用是唯一标识每一条记录。
    @GeneratedValue(strategy = GenerationType.IDENTITY) // @GeneratedValue 注解用于定义主键的生成策略，即如何自动生成主键的值。strategy = GenerationType.IDENTITY 表示使用数据库的自增主键策略（例如，MySQL 中的 AUTO_INCREMENT）。这意味着当你插入一条新记录时，数据库将自动为主键生成一个唯一的值
    private Long id;

    private String username;

    private String password;
}
