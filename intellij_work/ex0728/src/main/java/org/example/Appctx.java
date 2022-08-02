package org.example;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration // spring 객체 담는 통
public class Appctx {

    @Bean
    public ChangePwdService changePwdService(){
        return new ChangePwdService();
    }
    @Bean
    public MemberService memberService(){
        return new MemberService();
    }

    @Bean
    public MemberDao memberDao(){
        return new MemberDao();
    }

//    @Bean
//    public MemberDao memberDao1(){
//        return new MemberDao();
//    }
//
//    @Bean
//    public MemberDao memberDao2(){
//        return new MemberDao();
//    }

}
