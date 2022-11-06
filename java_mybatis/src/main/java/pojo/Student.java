package pojo;

import lombok.Data;

/**
 * @Author crisimple
 * @File Student
 * @Time 2021-04-08 23:42
 * @Description
 */
@Data
public class Student {

    private int id;
    private String studentName;
    private int tid;

    // 多个学生对应一个老师
    private Teacher teacher;
}
