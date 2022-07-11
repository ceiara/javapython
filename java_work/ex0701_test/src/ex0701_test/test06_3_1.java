package ex0701_test;

public class test06_3_1 {

	public static double carea(double r) {
		return r*r*3.14;
	}
	
	public static double cround(double r) {
		return 2*3.14*r;
	}
	
	public static void main(String[] args) {
		System.out.println("carea = "+carea(3));
		System.out.println("cround = "+cround(3));
		
	}
}
