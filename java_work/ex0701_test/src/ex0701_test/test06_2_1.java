package ex0701_test;

public class test06_2_1 {

	public static void area(int r) {
		double result = r*r*3.14;
		System.out.println("넓이: "+result);
	}
	
	public static void circle(int r) {
		double result = 2*r*3.14;
		System.out.println("둘레: "+result);
	}
	public static void main(String[] args) {
		area(8);
		circle(10);
		
	}
}
