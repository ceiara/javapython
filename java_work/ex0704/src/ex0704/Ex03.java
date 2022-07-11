package ex0704;

public class Ex03 {

	// test06_3_1
	/*
	 * 2^3 = 2*2*2*1
	 * 2^4 = 2*2*2*2*1
	 * 2^5 = 2*2*2*2*2*1
	 */
	public static void main(String[] args) {
		int result = doA(3);
		System.out.println("result = "+result);
		result = doA(5);
		System.out.println("result = "+result);
	}
	/*
	 * doA(3) 
	 * 2*doA(2)
	 * 2*2*doA(1)
	 * 2*2*2*doA(0)
	 * 2*2*2*1
	 */

	public static int doA(int n) {
		if(n==0) 
			return 1;
		else 
			return 2*doA(n-1);
	}
}
