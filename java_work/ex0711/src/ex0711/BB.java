
package ex0711;

public class BB {

	int a = 10;
	BB() {
		this(20); //3
		System.out.println("기본생성자"); //6
	}
	
	BB(int a) {
		System.out.println("a생성자"); //4
		this.a = a; // 5	
	}

	@Override
	public String toString() {
		return "BB [a=" + a + "]";
	}
	// alt + shift +s -> +s
}
