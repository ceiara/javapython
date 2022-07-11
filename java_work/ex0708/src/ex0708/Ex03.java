package ex0708;

public class Ex03 {

	public static void doA() {
		System.out.println("DoA 메서드");
	}
	public void doB() {
		System.out.println("DoB 메서드");
	}
	
	public static void main(String[] args) {
		Ex03.doA();
		Ex03 ex03 = new Ex03(); // static 영역에 있지 않아 따로 객체를 생성해 준 후 호출할 수 있다.
		ex03.doB();
		// static 메서드는 바로 호출 가능
		// static 메서드가 아닌 것은 메모리 영역에 할당 해야지만 호줄 가능
	}
	
}
