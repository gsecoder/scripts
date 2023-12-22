package com.secoder.java_aipasser.controller;

import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AiCalendarController {

    @GetMapping("/")
    public String home(Model model){
        return "Welcome Aipasser";
    }

    /*
    * 登录相关的逻辑
    * */
    @GetMapping("/login")
    public String login(){
        return "login";
    }

    public String doLogin(@RequestParam String username, @RequestParam String password){
        return "login success";
    }
}
