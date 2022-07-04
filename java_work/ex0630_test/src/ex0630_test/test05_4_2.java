package ex0630_test;

public class test05_4_2 {

	public static void main(String[] args) {
		
		//문제2. 1~100 출력 이어서 거꾸로 100~1 출력, while문
				int num1 = 1;
				while(num1<101) {
					System.out.println(num1);
					num1++;
				}
				
		// 거꾸로
				int num2 = 100;
				while(0<num2 && num2<101) {
					System.out.println(num2);
					num2-=1;
				}
	}
}
