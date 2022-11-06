/**
 * @author sf
 * @file DependTest
 * @date 2021/10/17 4:17 下午
 * @description
 */

import org.testng.annotations.Test;

public class DependTest {
	
	@Test
	public void setupEnv(){
		System.out.println("This is set Env");
	}
	
	@Test(dependsOnMethods = {"setupEnv"})
	public void testMessage(){
		System.out.println("this is a test Message");
	}
}