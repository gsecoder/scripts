package ioc_before;

import org.junit.jupiter.api.Test;

/**
 * @Author secoder
 * @File UserServiceTest
 * @Time 2021-07-18 00:27
 * @Description
 */
public class UserServiceTest {

    @Test
    public void userServiceTest(){
        UserService userService = new UserServiceImpl();

        userService.getOracleUser();

        userService.getMysqlUser();


    }
}
