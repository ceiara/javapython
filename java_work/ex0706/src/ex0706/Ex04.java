package ex0706;

class Circle{
	private int rad; // 다른 class에서 값의 변경을 허용하지 않음 ex) c1.rad = 10;와 같은 경우를 방지
	final double PI = 3.14;
	public void printArea() {
		System.out.println("넓이는 = "+PI*rad*rad);
	}
	public int getRad() {
		return rad;
	}
	public void setRad(int rad) {
		if (rad < 0) {
			System.out.println("반지름은 음수가 없습니다");
			return;
		}
		this.rad = rad;
	}
	public double getPI() {
		return PI;
	}
}

public class Ex04 {

	public static void main(String[] args) {
		Circle c1 = new Circle();
		c1.setRad(10);
		//c1.rad = 10;
		
		
	}
}
