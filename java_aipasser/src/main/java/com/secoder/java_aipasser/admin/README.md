# java_aicalender

## 数据库创建
```mysql
SHOW DATABASES;

CREATE DATABASE aipasser;

USE aipasser;
-- 用户信息表
CREATE TABLE user (
  id BIGINT AUTO_INCREMENT PRIMARY KEY COMMENT '主键',
  username VARCHAR(255) NOT NULL COMMENT '用户名',
  password VARCHAR(255) NOT NULL COMMENT '用户密码'
) ENGINE=InnoDB COMMENT='用户信息表';

-- 代办事项表
CREATE TABLE todo_item (
   id BIGINT AUTO_INCREMENT PRIMARY KEY COMMENT '主键。',
   title VARCHAR(255) NOT NULL COMMENT '待办事项标题。',
   date DATE NOT NULL COMMENT '待办事项日期。'
) ENGINE=InnoDB COMMENT='待办事项表';
```

## 问题记录
1、启动SpringBoot后，服务没有监听到配置的server.port
```text
解决方案：https://www.cnblogs.com/fruitknife/p/12560274.html
排查日志发现tomcat没有启动，导致端口没有被监听；那么为什么tomcat没有被监听呢，发现是因为pom.xml中少配置了start-web的依赖
```