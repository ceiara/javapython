package com.dip.org.confige;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration //환경을 잡는 package
@ComponentScan(basePackages = {"com.dip.org.member"})
public class AppConfig {

}
