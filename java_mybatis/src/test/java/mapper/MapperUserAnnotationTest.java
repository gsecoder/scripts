package mapper;

import org.apache.ibatis.session.SqlSession;
import org.junit.Test;
import util.MyBatisUtil;
import pojo.User;
import java.util.List;
/**
 * @Author secoder
 * @File MapperUserAnnotationTest
 * @Time 2021-04-07 20:15
 * @Description
 */
public class MapperUserAnnotationTest {

	SqlSession sqlSession = MyBatisUtil.getSession();
	// 本质上利用了jvm的动态代理机制
	UserAnnotationMapper userAnnotationMapper = sqlSession.getMapper(UserAnnotationMapper.class);

	// 查询所有用户
	@Test
	public void selectAllUserTest(){

		List<User> userList = userAnnotationMapper.selectAllUser();
		for (User user : userList) {
			System.out.println("user: " + user);
		}

		sqlSession.close();
	}


	// 根据ID查询用户
	@Test
	public void selectUserByIdTest(){

		User user = userAnnotationMapper.selectUserById(1);
		System.out.println(user);

		sqlSession.close();
	}


	// 新增用户
	@Test
	public void addUserTest(){

		User user = new User(6, "刘小六", "666666");
		int i = userAnnotationMapper.addUser(user);
		System.out.println("i: " + i);

		sqlSession.close();
	}


	// 修改用户
	@Test
	public void updateUserTest(){

		User user = new User(6, "刘小666", "6666");
		int i = userAnnotationMapper.updateUser(user);
		System.out.println("i: " + i);

		sqlSession.close();
	}


	// 删除用户
	@Test
	public void deleteUserTest(){

		int i = userAnnotationMapper.deleteUser(6);
		System.out.println("i: " + i);

		sqlSession.close();
	}
}
