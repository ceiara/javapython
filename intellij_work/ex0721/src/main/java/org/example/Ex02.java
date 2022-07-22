package org.example;

class A{

    // 인스턴스 메서드
    public void doA() {
        System.out.println("doA");
    }
    public static void doB() {
        System.out.println("doB");
    }
}

public class Ex02 {
    public static void main(String[] args) {
        Integer i1 = Integer.valueOf(3);
        Integer i2 = Integer.valueOf(10);

        // maxvalue,minvalue,sumvalue - static method
        int maxvalue = Integer.max(i1,i2);
        System.out.println(maxvalue);
        int minvalue = Integer.min(i1, i2);
        System.out.println(minvalue);
        int sumvalue = Integer.sum(i1, i2);
        System.out.println(sumvalue);

        System.out.println("2진수"+Integer.toBinaryString(i1)); // toBinaryString - static method
        System.out.println("8진수"+Integer.toOctalString(i2));
        System.out.println(Integer.toHexString(i2));

//      A.doA();(x) 클래스 A는 객체를 생성해야 호출할 수 있다.
        A a = new A();
        a.doA();

        // static은 메소드 영역에 있으므로 바로 호출 가능
        A.doB();
    }
}
