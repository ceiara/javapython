package ex0701_test;

public class test06_1_1 {

	public static void doA(int num1, int num2) {
		System.out.println("합 = " + (num1 + num2));
		System.out.println("차 = " + (num1 - num2));
		System.out.println("곱 = " + num1 * num2);
		System.out.println("몫 = " + num1 / num2);
		System.out.println("나머지 = " + num1 % num2);
//		return num2;
	}

	public static void main(String[] args) {
		doA(20, 7);

	}
}
