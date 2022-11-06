import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.time.Duration;
import java.time.temporal.ChronoUnit;

/**
 * @Author sf
 * @File JunitAssertTest
 * @Time 2021-07-08 20:13
 * @Description
 */
public class JunitAssertTest {
	
	@DisplayName("assertAll：断言分组")
	@Test
	void test_group_assertions(){
		int[] numbers = {0, 1, 2, 3, 4};
		Assertions.assertAll("numbers",
				() -> Assertions.assertEquals(numbers[1], 1),		
				() -> Assertions.assertEquals(numbers[2], 2),		
				() -> Assertions.assertEquals(numbers[4], 3)		
		);
	}
	
	@DisplayName("assertTimoutPreemptively：超时操作的测试")
	@Test
	void test_should_complete_in_one_second(){
		Assertions.assertTimeoutPreemptively(
				Duration.of(1, ChronoUnit.SECONDS), () -> Thread.sleep(1500)
		);
	}
	
	@DisplayName("assertThrows：异常测试")
	@Test
	void assert_throws_exception(){
		String str = null;
		Assertions.assertThrows(
				IllegalArgumentException.class, () ->{
					Integer.valueOf(str);
				}
		);
	}
	
}
