package mapper;

import pojo.Student;
import pojo.Teacher;

import java.util.List;

public interface StudentMapper {

    // 多对一（方法一）：按查询嵌套处理
    List<Student> getStudent1();

    // 多对一（方法二）：按结果嵌套处理
    List<Student> getStudent2();

    // 给多对一获取老师
    public Teacher getTeacher(int id);
}
