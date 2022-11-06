package pojo;

import lombok.Data;

import java.util.List;

/**
 * @Author crisimple
 * @File Teacher
 * @Time 2021-04-08 23:42
 * @Description
 */
@Data
public class Teacher {

    private int id;
    private String teacherName;

    // 一个老师对应多个学生
    private List<Student> students;
}
