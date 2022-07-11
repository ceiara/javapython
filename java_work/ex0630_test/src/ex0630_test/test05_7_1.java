package ex0630_test;

public class test05_7_1 {

	public static void main(String[] args) {
		for(int i=2;i<9;i+=2) {
			for(int j=1;j<i+1;j++) {
				if(i==2) {
					System.out.println("2 * "+j+"="+i*j);
				} else if(i==4) {
					System.out.println("4 * "+j+"="+i*j);
				} else if(i==6) {
					System.out.println("6 * "+j+"="+i*j);
				} else {
					System.out.println("8 * "+j+"="+i*j);
				}
			}
		}
	}
}
