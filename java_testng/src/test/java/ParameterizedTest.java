import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

/**
 * @author sf
 * @file ParameterizedTest
 * @date 2021/10/17 3:45 下午
 * @description
 */

public class ParameterizedTest {
	
	@Test
	@Parameters("test1")
	public void ParamTest(String param1){
		System.out.println("This is " + param1);
	}
	
}
