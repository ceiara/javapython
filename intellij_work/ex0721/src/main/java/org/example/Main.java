package org.example;

public class Main {
    int a = 10;
    public static void showData(Object obj) {
        System.out.println(obj);
        System.out.println(obj.toString());
    }
    public static void main(String[] args) {
        Integer iInst1 = Integer.valueOf(3);
        Integer iInst2 = 5;

        showData(iInst1);
        showData(iInst2);
        showData(new Integer(100));


    }
}