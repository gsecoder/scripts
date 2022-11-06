package com.secode.spring_boot.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @Author secoder
 * @File HelloController
 * @Time 2021-07-11 17:02
 * @Description
 */
@RestController
public class HelloController {

    @RequestMapping("hello")
    public String hello(){
        return "Hello SpringBoot";
    }
}
