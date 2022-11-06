package mapper;

import org.apache.ibatis.session.RowBounds;
import org.apache.ibatis.session.SqlSession;
import org.apache.log4j.Logger;
import org.junit.Test;
import pojo.User;
import util.MyBatisUtil;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @Author crisimple
 * @File MapperTest
 * @Time 2021-04-04 16:28
 * @Description
 */
public class MapperTest {
    
    static Logger logger = Logger.getLogger(MapperTest.class);
    
    // log4j 日志测试
    @Test
    public void selectUserLogTest(){
        logger.info("info：进入selectUserLog方法");
        logger.debug("debug：进入selectUserLog方法");
        logger.error("error: 进入selectUserLog方法");
        
        SqlSession sqlSession = MyBatisUtil.getSession();
        UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
        
        List<User> userList = userMapper.selectUser();
        for (User user : userList) {
            System.out.println("user: " + user);
        }
        sqlSession.close();
    }

    // 查询全部的用户
    @Test
    public void selectUserTest(){
        SqlSession sqlSession = MyBatisUtil.getSession();

        // 方法一
        List<User> users = sqlSession.selectList("mapper.UserMapper.selectUser");
        for (User user : users) {
            System.out.println("user: " + user);
        }

        // 方法二
        UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
        List<User> users1 = userMapper.selectUser();
        for (User user1 : users1) {
            System.out.println("user1: " + user1);
        }

        // 关闭连接
        sqlSession.close();
    }
    
    // 根据参数条件查询用户
    @Test
    public void selectParamsUserTest(){
        SqlSession sqlSession = MyBatisUtil.getSession();
        UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
        User user = userMapper.selectParamsUser(1);
        System.out.println("user: " + user);
        sqlSession.close();
    }
    
    // 模糊匹配（LIKE）
    @Test
    public void selectLike1UserTest(){
        SqlSession sqlSession = MyBatisUtil.getSession();
        UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
        
        // LIKE方法一：在Java代码中添加sql通配符（在sql语句中拼接通配符，会引起sql注入） %' AND 1=1 AND '%'='
        // 添加sql通配符
        //String wildcardName = "%' AND 1=1 AND '%'=";
        //List<User> userList = userMapper.selectLikeUser(wildcardName);
        //for (User user : userList) {
        //    System.out.println(user);
        //}
        
        // LIKE方法二：在配置文件中配置好通配符
        String wildcardName1 = "王小";
        List<User> userList1 = userMapper.selectLikeUser(wildcardName1);
        for (User user : userList1) {
            System.out.println(user);
        }
    }
    
    // 万能的Map查询
    @Test
    public void selectMapUserTest(){
        SqlSession sqlSession = MyBatisUtil.getSession();
        UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
        Map<String, Object> map = new HashMap<String, Object>();
        map.put("username", "王小四");
        map.put("password", "444444");
        Map<String, Object> user = userMapper.selectMapUser(map);
        System.out.println("user: " + user);
    }
    
    // SQL层面利用LIMIT实现分页
    // 在测试类中传入参数测试
    // 推断：起始位置 =  （当前页面 - 1 ） * 页面大小
    @Test
    public void selectLimitUserTest(){
        SqlSession sqlSession = MyBatisUtil.getSession();
        UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
        
        // 第几页
        int currentPage = 1;
        // 每页显示几个
        int pageSize = 1;
        
        Map<String,Integer> map = new HashMap<String,Integer>();
        map.put("startIndex", ((currentPage-1)*pageSize));
        map.put("pageSize", pageSize);
        
        List<User> userList = userMapper.selectLimitUser(map);
        for (User user : userList) {
            System.out.println("user: " + user);
        }
        sqlSession.close();
    }
    
    // 分页查询（利用RowBounds在Java代码层面实现）
    @Test
    public void selectRowBoundsUserTest(){
        SqlSession sqlSession = MyBatisUtil.getSession();
        //UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
        
        // 第几页
        int startIndex = 2;
        // 每页查询条数
        int pageSize = 2;
    
        RowBounds rowBounds = new RowBounds((startIndex - 1) * pageSize, pageSize);
        //通过session.**方法进行传递rowBounds，[此种方式现在已经不推荐使用了]
        List<User> userList = sqlSession.selectList("mapper.UserMapper.selectRowBoundsUser", null, rowBounds);
        for (User user : userList) {
            System.out.println("user: " + user);
        }
        sqlSession.close();
    }
    
    
    // 增加用户
    @Test
    public void addUserTest(){
        SqlSession sqlSession = MyBatisUtil.getSession();
        UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
        User user = new User(4, "王小五", "555555");
        User user1 = new User(5, "王小五", "555555");
        int i = userMapper.addUser(user);
        int i1 = userMapper.addUser(user1);
        System.out.println("i: " + i);
        System.out.println("i: " + i1);
        
        // 提交事务,重点!不写的话不会提交到数据库
        sqlSession.commit();
        sqlSession.close();
    }
    
    // 更新用户
    @Test
    public void updateUserTest(){
        SqlSession sqlSession = MyBatisUtil.getSession();
        UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
        try {
            User user = userMapper.selectParamsUser(4);
            user.setPassword("444444");
            int i = userMapper.updateUser(user);
            System.out.println("i: " + i);
            sqlSession.commit(); // 提交事务
            User userSelect = userMapper.selectParamsUser(4);
            System.out.println("userSelect: " + userSelect);
        }catch (Exception e){
            System.out.println(e);
        }finally {
            sqlSession.close();   
        }
    }
    
    // 删除用户
    @Test
    public void deleteUserTest(){
        SqlSession sqlSession = MyBatisUtil.getSession();
        try{
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
            int i = userMapper.deleteUser(3);
            System.out.println("i: " + i);
            sqlSession.commit();
            
            // 查询删除后的用户表用户是否被删除，进行检验
            List<User> userList = userMapper.selectUser();
            for (User user : userList) {
                System.out.println("user: " + user);
            }
            
        }catch (Exception e){
            System.out.println(e.fillInStackTrace());
        }finally {
            sqlSession.close();
        }
    }
}
