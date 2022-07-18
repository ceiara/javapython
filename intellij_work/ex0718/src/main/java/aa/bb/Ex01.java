package aa.bb;
interface AA{
    int AAA = 345; // public static final이 생략되어 있다.
    void doA();
}
// 첫번째 방법
class AAA implements AA{
    public void  doB(int a,String b,AA cc){

    }
    @Override
    public void doA() {
        System.out.println("AAA 클래스 안에 doA메서드");
    }
}
/*
    1. class를 만들어서 상속받아 재정의 하는 방법
    2. new AA() 인터페이스 생성과 동시에 메서드 재정의 하는 방법
 */
public class Ex01 {
    public static void main(String[] args) {

        System.out.println(AA.AAA);
        AAA a1 = new AAA(); // java 1.4
        a1.doA();
        new AA() {
            @Override
            public void doA() {
                System.out.println("AA 인터페이스 안에 doA메서드");
            }
        }.doA(); // java 1.6 - doA를 한번만 사용할 경우
        AA a3 = ()->{
            System.out.println("a3람다 안에 doA메서드"); // 람다는 선언과 동시에 사용
        };
        a3.doA();

    }
}
