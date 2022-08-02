package org.example;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration // spring 객체 통을 담는 class 라는 것을 알려줌
public class Config1 {

    @Bean
    public A a(){
        return new A();
    }
}
