package org.example;

import java.util.Random;

public class Ex03 {
    public static void main(String[] args) {
        System.out.println(System.currentTimeMillis());
        Random random = new Random(); // real random
        System.out.println("밀리세컨드 랜덤 시작");

        for (int i=0; i<10; i++){
            System.out.println(random.nextInt(100));
        }
        System.out.println("밀리세컨드 랜덤 끝");

        Random randomseed = new Random(42); // random 이지만 pattern 정해져 있음
        System.out.println("씨드 랜덤 시작");
        for (int i =0; i<10; i++){
            System.out.println(randomseed.nextInt(100));
        }
        System.out.println("씨드 랜덤 끝");

    }
}
