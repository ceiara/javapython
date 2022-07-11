package ex0706;

/*
 * 생성자를 포함하는 클래스의 정의
 * 삼각형
 */
class Triangle{
	int width;
	int height;

	public Triangle() {}	
	public Triangle(int width, int height) {
		super();
		this.width = width;
		this.height = height;
	}

	// alt +shift  + s -> o 생성자
	// alt + shift + s -> r getter setter 만들기
	
	public void printArea() {
		double area = this.width* this.height * 0.5d; // this 생략 가능
		System.out.println("넓이는 = "+area);
	}
	
	public void setWidth(int w) {
		width = w;
	}
	
	public void setHeight(int height) {
		this.height = height;
	}
}
public class Ex01 {
	public static void main(String[] args) {
		Triangle t1 =  new Triangle();
		t1.printArea();
		t1.setHeight(50);
		t1.setWidth(50);
		t1.printArea();
		
		Triangle t2 = new Triangle(30,50);
		t2.printArea();
	}
}
