package ex0705;

/*
 * 밑변과 높이 정보를 저장할 수있는 Triangle 클래스 정의(그 안에 적절한 생성자도 정의).
 * 그리고 밑변과 높이 정보를 변경 할 수 있는 메소드와 삼각형의 넓이를 계산해서 반환하는 메소드도 함께 정의.
 * 물론 이 클래스의 활용의 예를 보이는 main 메소드도 함께 작성.
 */
public class test_7_1 {
	
	public static void main(String[] args) {
		Triangle a1 = new Triangle(0, 0);
		a1.change(8, 10);
		a1.tarea(8, 10);
		a1.printres();
	}
}
