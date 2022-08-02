package org.example;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Import;

@Configuration
@Import(ImportConfig.class) //
public class ClassConfig {

    // 생성자에 의한 DI 방식
//    @Bean
//    public MemberService memberService() {
//        return new MemberService(memberDAO());
//    }
    // setter에 의한 DI 방식
    @Bean
    public MemberService memberService() {
        MemberService ms = new MemberService();
//        ms.setMemberDAO(memberDAO);
//        ms.setMemberPrinter(memberPrinter);
        return ms;
    }
}
