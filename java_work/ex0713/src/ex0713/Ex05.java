package ex0713;

class AA{
	AA() {
		System.out.println("AA 기본생성자");
	}
}

class BB extends AA {
	BB() {
		super(); // 부모클래스 호출, 생략가능
		System.out.println("BB 기본생성자"); //생략가능
	}
}

public class Ex05 {
	public static void main(String[] args) {
		new BB(); // 기본생성자 호출
	}
}
