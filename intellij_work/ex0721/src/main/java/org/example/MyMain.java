package org.example;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class MyMain {
    public static void main(String[] args) {
        // 원래 java 문법 - 다른 공간 사용
        Greeter g1 = new Greeter();
        Greeter g2 = new Greeter();

        System.out.println(g1);
        System.out.println(g2);
        System.out.println(g1==g2);

        // spring 통 안에 greeter(class)을 담아 쓰는것 - 같은 공간을 사용하여 메모리의 낭비가 없다
        AnnotationConfigApplicationContext acac =
                new AnnotationConfigApplicationContext(AppContext.class);

        Greeter g3 = acac.getBean(Greeter.class);
        Greeter g4 = acac.getBean(Greeter.class);

        System.out.println(g3);
        System.out.println(g4);
        System.out.println(g3==g3);

        acac.close();
    }
}
