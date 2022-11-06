package ioc_di_after;

/**
 * @Author secoder
 * @File UserDaoMysqlImpl
 * @Time 2021-07-18 12:00
 * @Description
 */
public class UserDaoImpl implements UserDao {

    @Override
    public void getUser(){
        System.out.println("Dao获取用户数据");
    }
    
}
