package mapper;

import org.apache.ibatis.session.SqlSession;
import org.junit.Test;
import pojo.Student;
import pojo.Teacher;
import util.MyBatisUtil;

import java.util.List;

/**
 * @Author crisimple
 * @File SchoolTest
 * @Time 2021-04-09 00:16
 * @Description
 */
public class SchoolTest {

    SqlSession sqlSession = MyBatisUtil.getSession();

    @Test
    public void getStudent1Test(){
        StudentMapper studentMapper = sqlSession.getMapper(StudentMapper.class);

        List<Student> students = studentMapper.getStudent1();

        for (Student student : students) {
            System.out.println( student
//                    "学生：" + student.getStudentName()
//                    + "\t 老师：" + student.getTeacher().getTeacherName()
            );
        }
    }

    @Test
    public void getStudent2Test(){
        StudentMapper studentMapper = sqlSession.getMapper(StudentMapper.class);

        List<Student> students = studentMapper.getStudent2();

        for (Student student : students) {
            System.out.println( student
//                    "学生：" + student.getStudentName()
//                    + "\t 老师：" + student.getTeacher().getTeacherName()
            );
        }
    }

    @Test
    public void getTeacher1Test(){
        TeacherMapper teacherMapper = sqlSession.getMapper(TeacherMapper.class);

        Teacher teacher = teacherMapper.getTeacher1(1);
        System.out.println(teacher.getTeacherName());
        System.out.println(teacher.getStudents());

    }

    @Test
    public void getTeacher2Test(){
        TeacherMapper teacherMapper = sqlSession.getMapper(TeacherMapper.class);

        Teacher teacher = teacherMapper.getTeacher2(1);
        System.out.println(teacher.getTeacherName());
        System.out.println(teacher.getStudents());

    }
}
