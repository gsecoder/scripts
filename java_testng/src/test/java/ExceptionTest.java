/**
 * @author secoder
 * @file ExceptionTest
 * @date 2021/10/17 3:23 下午
 * @description
 */

import org.testng.annotations.Test;

public class ExceptionTest {
	
	@Test(expectedExceptions = IllegalArgumentException.class, expectedExceptionsMessageRegExp = "NullPoint")
	public void testException(){
		throw new IllegalArgumentException("NullPoint");
	}
	
	public static void main(String[] args) {
		// main 方法
	}
}
