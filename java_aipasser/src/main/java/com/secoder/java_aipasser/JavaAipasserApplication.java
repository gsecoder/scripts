package com.secoder.java_aipasser;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.scheduling.annotation.EnableAsync;

@SpringBootApplication
@EnableAsync
@EntityScan("com.secoder.java_aipasser.model")
public class JavaAipasserApplication {
	public static void main(String[] args) {
		ConfigurableApplicationContext context =  SpringApplication.run(JavaAipasserApplication.class, args);

		//// 主线程等待
		//try {
		//	// 这里可以执行一些其他操作
		//	Thread.sleep(Long.MAX_VALUE);
		//} catch (InterruptedException e) {
		//	e.printStackTrace();
		//} finally {
		//	// 在关闭应用程序时执行一些清理操作
		//	context.close();
		//}
	}

}
