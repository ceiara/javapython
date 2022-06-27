package ex0627;

// 예제 CondOp.java를 조건 연산자를 사용하지않고 if ~ else문을 사용하는 형태로 수정해보자.

public class test_05_2 {

	public static void main(String[] args) {
		int num1 = 50;
		int num2 = 100;
		// 문제
		int big;
		int diff;
		
		big = (num1 > num2) ? num1 : num2;
		System.out.println("큰 수: " + big);
		
		diff = (num1 > num2) ? (num1 - num2) : (num2 - num1);
		System.out.println("절대값: " + diff);
		
		// 답
		if(num1>num2) 
			System.out.println(num1);
		else
			System.out.println(num2);
		
		if(num1>num2)
			System.out.println(num1 - num2);
		else
			System.out.println(num2 - num1);
		
	}
	
}
