package ex0708;

class Point {
	int xPos, yPos;

	public Point(int xPos, int yPos) { // 생성자
		this.xPos = xPos;
		this.yPos = yPos;
	}
	public void showPointInfo() {
		System.out.println("["+xPos+" , "+yPos+"]");
	}
}

public class Circle {
	
	Point point; // 변수 선언
	int r;
	public Circle(int i, int j, int k) {
		point = new Point(i,j); 
		this.r = k;
	}

	private void showCircleInfo() {
		System.out.println("반지름 r = "+ this.r);
		point.showPointInfo();
	}
	public static void main(String[] args) {
		Circle circle = new Circle(2,2,4);
		circle.showCircleInfo();
	}
	
}
