package ex0713;

public class Quiz13_2_2 {

	public static void main(String[] args) {
		int a[][] = new int[3][3];
		
		int num = 1;
		for(int i=0; i<a.length; i++) {
			for(int j=0; j<a[i].length;j++) {
				a[i][j] = num;
				num++;
			}
		}
		for(int i=0; i<a.length; i++) {
			for(int j=0; j<a[i].length; j++) {
				if (i==0) { 
					a[0][j] = a[2][j];
				}
				if (i==2) {
					a[2][j] = a[1][j];
				}
				System.out.print(a[i][j]+"\t");
			}
			System.out.println();
		}
	}	
}