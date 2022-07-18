package aa.bb;

public class Ex04 {
    public static void main(String[] args) {
        try {
            doA();
        } catch (Exception e) {
            System.out.println("내가 호출한 메서드 호출 문제");
        }
    }
    // throws Exception: 예외가 발생하면 doA에서 호출한 지역에서 알아서 처리해라
    // 다른 개발자와 함께 개발하는데 나 말고 다른 개발자 코드에 문제가 있을 경우 조금이라도 에러 발생 위치를 알려주는 역할을 할 수 있음
    public static void doA()throws Exception {
        System.out.println("doA메서드에서 예외발생할 수도 있음");
    }
}
