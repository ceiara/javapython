package org.config;

import org.member.MemberDao;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration //환경을 잡는 package
@ComponentScan(basePackages = {"org.member"})
public class AppConfig {

//	@Bean
//	public MemberDao memberDao() {
//		return new MemberDao();
//	}
	
	
//	@Bean
//	public MemberService memberService() {
//		return new MemberService();
//	}
}