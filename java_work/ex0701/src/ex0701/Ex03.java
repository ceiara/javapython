package ex0701;

import java.util.Scanner;

public class Ex03 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("첫번째 수 입력");
		int num1 = scan.nextInt();
		System.out.println("두번째 수 입력");
		int num2= scan.nextInt();
		division(num1, num2);
	}
	
	public static void division(int n1, int n2) {
		System.out.println("n1/n2 = "+n1/n2);
	}
}
