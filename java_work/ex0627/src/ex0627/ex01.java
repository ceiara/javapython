package ex0627;

public class ex01 {

	
	public static void main(String[] args) {
		
		// 변수 선언
		// 변수의 사용 용도에 따라
		// int double String boolean
		// 형변환 자동형변환 수동형변환
		int a = 10;
		double b = a;
		
		double c = 30.44;
		int d = (int)c; // double를 int라는 작은 공간 안에 넣어야 하기 때문에 수동으로 변환해야 한다.
		System.out.println("b = "+b);
		System.out.println("d = "+d);
		
		System.out.println("(3+4)*5 = "+(3+4)*5);
		System.out.println("3>4 = "+(3>4));
		
		int num1 = 3;
		System.out.println("3>4 = "+(3>4 && (num1+=3)<3));
		System.out.println("num1 = "+ num1);
		System.out.println("3>4 = "+(3>4 || (num1+=3)<3));
		System.out.println("num1 = "+ num1);
		
	}
}
