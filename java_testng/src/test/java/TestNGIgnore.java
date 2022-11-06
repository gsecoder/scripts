/**
 * @author sf
 * @file TestNGIgnore
 * @date 2021/10/17 4:08 下午
 * @description
 */

import org.testng.annotations.Test;

public class TestNGIgnore {
	
	@Test(enabled = false)
	public void testIgnore(){
		System.out.println("This test will be ignore.");
	}
}
