package ex0711;

public class Ex03 {

	public Ex03() {
		System.out.println("기본생성자");
	}
	public Ex03(int a) {
		System.out.println("파라메터 1개 a = "+a);
	}
	public Ex03(int a, int b) {
		System.out.println("파라메타 2개 a = "+a);
		System.out.println("파라메타 2개 b = "+b);
	}
	// 이름이 같은 다른 생성자를 생성하게 되면 기본 생성자를 생략할 수 없게 된다.
	public static void main(String[] args) {
		new Ex03(); // 가르키는 것이 없기 떄문에 객체 생성과 동시에 소멸 
		new Ex03(10);
		new Ex03(10,20);
	}
}
