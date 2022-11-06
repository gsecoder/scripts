package mapper;

import org.apache.ibatis.session.SqlSession;
import org.junit.Test;
import pojo.User;
import util.MyBatisUtil;

/**
 * @Author crisimple
 * @File SQLCacheTest
 * @Time 2021-04-10 14:01
 * @Description
 */
public class SQLCacheTest {

    @Test
    public void selectUserById(){

        SqlSession sqlSession = MyBatisUtil.getSession();
        SQLCacheMapper sqlCacheMapper = sqlSession.getMapper(SQLCacheMapper.class);

        // 执行完看日志发现，这里的SQL语句只查询了一次，第二次结果没有进行数据库查询，用的是同一个对象
        User user = sqlCacheMapper.selectUserById(1);
        System.out.println(user);

        sqlSession.clearCache();//手动清除缓存

        User user1 = sqlCacheMapper.selectUserById(1);
        System.out.println(user1);
        System.out.println(user == user1);

        sqlSession.close();

    }

    @Test
    public void selectUserByIdTwoCacheTest(){

        SqlSession sqlSession1 = MyBatisUtil.getSession();
        SqlSession sqlSession2 = MyBatisUtil.getSession();
        SQLCacheMapper sqlCacheMapper1 = sqlSession1.getMapper(SQLCacheMapper.class);
        SQLCacheMapper sqlCacheMapper2 = sqlSession2.getMapper(SQLCacheMapper.class);

        User user1 = sqlCacheMapper1.selectUserById(1);
        System.out.println(user1);
        sqlSession1.close();

        User user2 = sqlCacheMapper2.selectUserById(1);
        System.out.println(user2);
        System.out.println(user1 == user2);

        sqlSession2.close();

    }
}
