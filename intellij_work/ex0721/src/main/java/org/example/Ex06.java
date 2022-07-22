package org.example;

class MySingle{
    public static MySingle ms;
    public MySingle getInstane() {
        if(ms == null){
            ms = new MySingle();
            return ms;
        }else {
            return ms;
        }
    }
    public void doA(){
        System.out.println("doA");
    }
}

public class Ex06 {
    Ex06(){
        MySingle ms1 = new MySingle();
        ms1.doA();
        MySingle ms2 = new MySingle();
        ms2.doA();
        System.out.println(ms1);
        System.out.println(ms2);


    }

    public static void main(String[] args) {
        new Ex06();
    }
}
