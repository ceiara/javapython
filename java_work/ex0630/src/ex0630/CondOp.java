package ex0630;

/*
 * 두개의 수를 선언하고 
 * 두수 중에 큰 수를 삼항연산자 출력하고
 * 두수의 차를 절대값
 */

public class CondOp {

	public static void main(String[] args) {
		
		int num1 = 50;
		int num2 = 100;
		int result = 0;
		
		if(num1 > num2) {
			result = num1;
		} else {
			result = num2;
		}
		System.out.println(("result = "+ result));
		
		if(num1 > num2) {
			result = num1 - num2;
		} else {
			result = num2 - num1;
		}
		System.out.println(("result = "+ result));
		
//		System.out.println("num1 "+ num1);
//		System.out.println("num2 "+ num2);
		
//		int result = num1>num2? num1:num2;
//		System.out.println("result = "+ result);
		
		result = num1>num2? num1-num2 : num2-num1;
		System.out.println("result = "+ result);
		
	}
	
}
