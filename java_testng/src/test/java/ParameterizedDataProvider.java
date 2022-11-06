/**
 * @author sf
 * @file ParameterizedDataProvider
 * @date 2021/10/17 4:03 下午
 * @description
 */

import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

public class ParameterizedDataProvider {
	
	@DataProvider
	public Object[][] Users(){
		return new Object[][]{
                {"root","passowrd"},
                {"cnblogs.com", "tankxiao"},
                {"tank","xiao"}
        };
	}
	
	@Test(dataProvider="user")
    public void verifyUser(String userName, String password){
        System.out.println("Username: "+ userName + " Password: "+ password);
    }
}
