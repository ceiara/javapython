package ex0624;

public class test {
	public static void main(String[] args) {
		// 문제 1
		int num1 = 10;
		int num2 = 20;
		int num3 = 30;
		
		num1 = num2 = num3; // 값이 30이 나옴. num3가 2->1로 할당된다.
		
	  //System.out.println(num1 == num2 && num2 == num3);
		
		// 문제 2
		System.out.println(((25*5)+(36-4)-72)/5);
		
		// 문제 3
		/*
		int  = 3;
		int b = 6;
		int c = 9;
		int d = 12;
		
		System.out.println("3 + 6 = "+(a+b));
		System.out.println("3 + 6 + 9 = "+(a+b+c));
		System.out.println("3 + 6 + 9 + 12 = "+(a+b+c+d));
		*/
		
		int a = 3+6;
		System.out.println(a);
		a+=9;
		System.out.println(a);
		a+=12;
		System.out.println(a);
		
		// 문제 4
		int n1 = ((25+5)+(36/4)-72)*5;
		int n2 = ((25*5)+(36-4)+71)/4;
		int n3 = (128/4)*2;
				
		System.out.println(n1 > n2 && n2 > n3);
		
		
	}

}

