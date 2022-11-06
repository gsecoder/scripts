package mapper;


import pojo.Teacher;

public interface TeacherMapper {

    // 【一对多，按结果嵌套处理】获取老师对应的学生
    public Teacher getTeacher1(int id);

    // 【一对多，按查询嵌套处理】获取老师对应的学生
    public Teacher getTeacher2(int id);

    // 一对多，通过老师ID查询到对应的学生
    public Teacher getStudentByTeacherId(int id);
}
