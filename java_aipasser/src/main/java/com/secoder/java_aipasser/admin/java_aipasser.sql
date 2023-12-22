SHOW DATABASES;

CREATE DATABASE aipasser;

USE aipasser;
-- 用户信息表
CREATE TABLE user (
  id BIGINT AUTO_INCREMENT PRIMARY KEY COMMENT '主键',
  username VARCHAR(255) NOT NULL COMMENT '用户名',
  password VARCHAR(255) NOT NULL COMMENT '用户密码'
) ENGINE=InnoDB COMMENT='用户信息表';

INSERT INTO `user` (username, password)
VALUES
('Jone',   'Jone@159357'),
('Jack',   'Jack@159357'),
('Tom',    'Tom@159357'),
('Sandy',  'Sandy@159357'),
('Billie', 'Billie@159357');

-- 代办事项表
CREATE TABLE todo_item (
   id BIGINT AUTO_INCREMENT PRIMARY KEY COMMENT '主键。',
   title VARCHAR(255) NOT NULL COMMENT '待办事项标题。',
   date DATE NOT NULL COMMENT '待办事项日期。'
) ENGINE=InnoDB COMMENT='待办事项表';

