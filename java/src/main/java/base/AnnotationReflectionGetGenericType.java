package base; /**
 * @file base.AnnotationReflectionGetGenericType
 * @author sf
 * @date 2020/9/1 9:22 下午
 * @description 通过反射获取泛型
 */

import java.lang.reflect.Method;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.util.List;
import java.util.Map;

public class AnnotationReflectionGetGenericType {

// 参数化类型
public void test01(Map<String, StudentClass> map, List<StudentClass> list) {
	System.out.println("test01");
}

// 带返回值
public Map<String, StudentClass> test02() {
	System.out.println("test02");
	return null;
}

public static void main(String[] args) throws NoSuchMethodException {
	// main 方法
	
	Method method = AnnotationReflectionGetGenericType.class.getMethod("test01", Map.class, List.class);
	
	// 获取有参数的泛型
	Type[] genericParameterTypes = method.getGenericParameterTypes();
	for (Type genericParameterType : genericParameterTypes) {
		System.out.println("#" + genericParameterType);
		if(genericParameterType instanceof ParameterizedType) {
			Type[] actualTypeArguments = ((ParameterizedType) genericParameterType).getActualTypeArguments();
			System.out.println("获取有参数的泛型" + actualTypeArguments);
		}
	}
	
	// 获取有返回值的泛型
	Method method1 = AnnotationReflectionGetGenericType.class.getMethod("test02", null);
	Type genericReturnType = method1.getGenericReturnType();
	for (Type genericParameterType : genericParameterTypes) {
		Type[] actualTypeArguments = ((ParameterizedType) genericParameterType).getActualTypeArguments();
		System.out.println("获取有返回值的泛型" + actualTypeArguments);
	}
}
}
