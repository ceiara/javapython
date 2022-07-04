package ex0630_test;

public class test05_5_1 {

	// 1부터 10까지의 곱의 결과를 출력하는 for문
	public static void main(String[] args) {
		int sum = 1;
		for(int num=1;num<11;num++) {
			sum *= num;
		}
		System.out.println(sum);
	}
}
