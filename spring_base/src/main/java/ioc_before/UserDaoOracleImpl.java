package ioc_before;

/**
 * @Author secoder
 * @File UserDaoImpl
 * @Time 2021-07-18 00:22
 * @Description
 */
public class UserDaoOracleImpl implements UserDao{

    @Override
    public void getOracleUser(){
        System.out.println("UserDaoOracle2获取用户");
    }

    public void getMysqlUser(){
        System.out.println("UserDaoMysql2获取用户数据");
    }
}
