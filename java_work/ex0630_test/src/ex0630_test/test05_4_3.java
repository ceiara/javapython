package ex0630_test;

public class test05_4_3 {

	public static void main(String[] args) {

		// 문제3. 1000이하 2의 배수이자 7의 배수 출력하고 그 수의 합

		int num2 = 1;
		int sum = 0;
		while (num2 < 1001) {
			if (num2 % 2 == 0 && num2 % 7 == 0) {
				System.out.println("num2 = "+num2);
				sum += num2;
			}
			num2++;
		}
		System.out.println("sum = "+sum);
	}

}
