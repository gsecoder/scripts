package ioc_before;

/**
 * @Author secoder
 * @File UserDaoMysqlImpl
 * @Time 2021-07-18 12:00
 * @Description
 */
public class UserDaoMysqlImpl implements UserDao{

    @Override
    public void getOracleUser(){
        System.out.println("OracleDao1获取用户数据");
    }

    @Override
    public void getMysqlUser(){
        System.out.println("MysqlDao1获取用户数据");
    }
}
