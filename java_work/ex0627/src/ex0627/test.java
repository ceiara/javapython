package ex0627;

public class test {

	/*
	 * 아래의 코드에서는 두 개의 if문을 사용하고 있다. 이를 하나의 if문만 사용하도록 변경해보자. 
	 * class IfReit { 
	 * 		int num=120; 
	 * 		int(num > 0) { 
	 * 			if((num % 2)) == 0) 
	 * 				System.out.println("양수이면서 짝수"); 
	 * 			} 
	 * 		}
	 * }
	 */

	public static void main(String[] args) {
	
		int num = 120;
		
		if(num > 0) 
			System.out.println("양수");
		else if((num % 2) == 0)
			System.out.println("양수이면서 짝수");
	}

}
