package ioc_annotation;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Import;

/**
 * @Author sf
 * @File MyConfig
 * @Time 2021-03-30 20:43
 * @Description
 */
@Configuration  //代表这是一个配置类
@Import(MyConfig2.class)    //导入合并其他配置类，类似于配置文件中的 inculde 标签
public class MyConfig {
	
	//通过方法注册一个bean，这里的返回值就Bean的类型，方法名就是bean的id！
	@Bean
	public ConfigBase configBase(){
        return new ConfigBase();	
    }

}
