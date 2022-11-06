/**
 * @author secoder
 * @file TestSimpleTestNG
 * @date 2021/10/17 1:44 下午
 * @description
 */

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.testng.annotations.Test;

public class TestSimpleTestNG {
	
	@BeforeClass
	public void beforeClass(){
		System.out.println("this is before class");
	}
	
	@Test
	public void TestNGLearn(){
		System.out.println("This is TestNG Learn Test case");
	}
	
	@AfterClass
	public void afterClass(){
		System.out.println("this is after class");
	}
	
}
