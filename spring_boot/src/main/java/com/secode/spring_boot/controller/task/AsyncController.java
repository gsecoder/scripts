package com.secode.spring_boot.controller.task;

import com.secode.spring_boot.service.task.AsyncService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @Author secoder
 * @File AsyncController
 * @Time 2021-07-15 22:48
 * @Description
 */
@RestController
@RequestMapping("/task")
public class AsyncController {

    @Autowired
    AsyncService  asyncService;

    @GetMapping("/hello")
    public String hello(){
        asyncService.hello();
        return "success";
    }
}
