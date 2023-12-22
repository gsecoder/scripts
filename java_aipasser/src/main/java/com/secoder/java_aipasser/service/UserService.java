package com.secoder.java_aipasser.service;

import com.secoder.java_aipasser.model.User;
import com.secoder.java_aipasser.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    @Autowired(required=true)
    private PasswordEncoder passwordEncoder;


    /*
    * 添加用户
    * */
    public void saveUser(User user){
        user.setPassword(passwordEncoder.encode(user.getPassword()));
        userRepository.save(user);
    }

    /*
    * 查看用户-根据用户名称
    * */
    public User findByUsername(String username){
        return userRepository.findByUsername(username);
    }


}
