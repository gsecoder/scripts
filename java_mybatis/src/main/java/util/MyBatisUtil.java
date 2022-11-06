package util;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;
import java.io.InputStream;

/**
 * @Author crisimple
 * @File MyBatis
 * @Time 2021-04-04 15:39
 * @Description
 */
public class MyBatisUtil {

    private static SqlSessionFactory sqlSessionFactory;

    // static静态代码块在代码运行时已经加载了
    static {
        try {
            String resource = "mybatis-config.xml";
            InputStream inputStream = Resources.getResourceAsStream(resource);
            sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // 获取SqlSession连接
    public static SqlSession getSession(){
        return sqlSessionFactory.openSession();
    }
}
