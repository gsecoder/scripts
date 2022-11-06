import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

/**
 * @Author sf
 * @File JunitParamsTest
 * @Time 2021-07-08 20:51
 * @Description
 */
public class JunitParamsTest {
	
	@DisplayName("")
	@ParameterizedTest
	@CsvSource(value = {"1,one", "2,Two", "3,Three"})
	void test_dataFrom_csv(long id, String name){
		System.out.printf("id: %d, name: %s", id, name);
	}
	
}
