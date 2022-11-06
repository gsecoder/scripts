package ioc_before;

/**
 * @Author secoder
 * @File UserServiceImpl
 * @Time 2021-07-18 00:24
 * @Description
 */
public class UserServiceImpl implements UserService{

    private UserDao userOracleDao = new UserDaoOracleImpl();
    private UserDao userDaoMysql = new UserDaoMysqlImpl();

    @Override
    public void getOracleUser(){
        userOracleDao.getOracleUser();
    }

    public void getMysqlUser(){
        userDaoMysql.getMysqlUser();
    }

}
