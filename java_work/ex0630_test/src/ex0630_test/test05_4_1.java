package ex0630_test;

public class test05_4_1 {

	//문제1. while문을 이용하여 1부터 99까지의 합을 구하기 
		public static void main(String[] args) {
			int num = 0;
			int sum = 0;
			while(num < 100) {
				sum += num;
				num++;
			}
			System.out.println(sum);
		
		}
}
