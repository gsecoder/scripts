package com.secode.spring_boot.service.task;

import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

/**
 * @Author secoder
 * @File AsyncService
 * @Time 2021-07-15 22:34
 * @Description
 */
@Service
public class AsyncService {

    @Async  // 告诉Spring这是一个异步方法
    public void hello(){
        try{
            Thread.sleep(3000);
        }catch (InterruptedException e){
            e.printStackTrace();
        }

        System.out.println("业务进行中....");
    }
}
