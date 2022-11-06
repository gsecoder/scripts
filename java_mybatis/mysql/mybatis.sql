CREATE DATABASE `mybatis`;

USE `mybatis`;

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
    `id` int(20) NOT NULL,
    `username` varchar(30) DEFAULT NULL,
    `password` varchar(30) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert  into `user`(`id`,`username`,`password`)
values (1,'陈小杰','123456'),
       (2,'张小海','321456'),
       (3,'李小天','987654');

-- UPDATE user SET authentication_string='root@159357' WHERE user='root';
-- GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root@159357';
-- select  User,authentication_string,Host from user;
-- grant all privileges on *.* to admin@"%" identified by 'password' with grant option
-- grant all privileges on *.* to 'root'@'%' identified by 'password' with grant option;
-- update user set host = '%' where user = 'root';
-- grant all privileges on *.* to 'root'@'%' identified by 'password' with grant option;
-- flush privileges;
-- GRANT ALL PRIVILEGES ON mybatis.* TO 'admin'@'%' IDENTIFIED BY "password" WITH GRANT OPTION;
-- grant all privileges on mybatis.* to 'admin'@"%" identified by "password";

-- 多对一【多个学生对应一个老师】
CREATE TABLE `teacher`(
    `id` INT(10) NOT NULL,
    `teacher_name` VARBINARY(30) DEFAULT NUll,
    PRIMARY KEY (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

INSERT INTO teacher(`id`, `teacher_name`)VALUES (1, 'TeacherLuo');


CREATE TABLE `student` (
    `id` INT(10) NOT NULL,
    `student_name` VARCHAR(30) DEFAULT NULL,
    `tid` INT(10) DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `fktid` (`tid`),
    CONSTRAINT `fktid` FOREIGN KEY (`tid`) REFERENCES `teacher` (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

INSERT INTO student(`id`, `student_name`, `tid`)
VALUES ('1', '小明', NULL),
       ('2', '小红', NULL),
       ('3', '小李', NULL),
       ('4', '小张', NULL),
       ('5', '小王', NULL);

-- 多对一（获取所有学生及对应老师的信息）
SELECT * FROM mybatis.student 
WHERE tid IN (
    SELECT DISTINCT teacher.id FROM mybatis.teacher WHERE tid=1
);
SELECT teacher.teacher_name
FROM mybatis.student, mybatis.teacher
WHERE student.tid = teacher.id;


-- 【动态SQL】
-- 新建一个数据库表：blog
CREATE TABLE `blog`(
    `id` VARCHAR(50) NOT NULL COMMENT '博客ID',
    `title` VARCHAR(100) NOT NULL COMMENT '博客标题',
    `author` VARCHAR(30) NOT NULL COMMENT '博客作者',
    `create_time` DATETIME NOT NULL COMMENT '创建时间',
    `views` INT(30) NOT NULL COMMENT '浏览量'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;






