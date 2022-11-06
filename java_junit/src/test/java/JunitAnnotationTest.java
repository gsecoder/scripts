import org.junit.jupiter.api.*;

/**
 * @Author secoder
 * @File JUnitTest.java
 * @Time 2021-07-05 23:38
 * @Description
 */
@DisplayName("这是我的JUnit测试类")
public class JunitAnnotationTest {

    @BeforeAll
    public static void init(){
        System.out.println("初始化数据");
    }

    @AfterAll
    public static void cleanup(){
        System.out.println("清理数据");
    }

    @BeforeEach
    public void tearup(){
        System.out.println("当前测试方法开始");
    }

    @AfterEach
    public void teardown(){
        System.out.println("当前测试方法结束");
    }

    @DisplayName("这是我的第1个测试方法")
    @Test
    void TestFirstCase(){
        System.out.println("这是我的第1个测试方法");
    }

    @DisplayName("这是我的第2个测试方法")
    @Test
    void TestSecondCase(){
        System.out.println("这是我的第2个测试方法");
    }

    @Disabled
    @DisplayName("这是我的第3个测试方法")
    @Test
    void TestThirdCase(){
        System.out.println("这是我的第3个测试方法");
    }

    @DisplayName("重复性测试方法")
    @RepeatedTest(value = 3, name = "{DisplayName} 第 {currentRepetition} 次")
    void TestFourthRepeated(){
        System.out.println("重复性测试方法");
    }

    @Nested
    @DisplayName("这是第一个内嵌测试类")
    class FirstNestedClass{
        @Test
        @DisplayName("第1个内嵌测试类的测试方法")
        void nestedFirstMethod(){
            System.out.println("第1个内嵌测试类的测试方法");
        }
    }

    @Nested
    @DisplayName("这是第二个内嵌测试类")
    class SecondNestedClass{
        @Test
        @DisplayName("第2个内嵌测试类的测试方法")
        void nestedFirstMethod(){
            System.out.println("第2个内嵌测试类的测试方法");
        }
    }
}
