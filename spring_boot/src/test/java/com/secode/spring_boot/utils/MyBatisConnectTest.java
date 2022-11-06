package com.secode.spring_boot.utils;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import javax.sql.DataSource;

/**
 * @Author secoder
 * @File MyBatisConnectTest
 * @Time 2021-07-13 20:48
 * @Description
 */
@SpringBootTest
public class MyBatisConnectTest {
	
	@Autowired
	DataSource dataSource;
	
	@Test
	void connectTest(){
		System.out.println("dataSource: " + dataSource);
	}
}
