package ex0630_test;

public class test05_6_2 {

	public static void main(String[] args) {
		
		int num = 1;
		int sum = 0;
		while(true) {
			sum += num;
			num += 2;
			System.out.println("num = "+num);
			if(sum>1000)
				break;
		}
		System.out.println("sum = "+sum);
	}
}
