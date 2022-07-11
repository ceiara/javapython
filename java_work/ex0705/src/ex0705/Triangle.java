package ex0705;

public class Triangle {
	int baseline;
	int height;
	double result;
	
	public Triangle(int bl, int h) {
		baseline = bl;
		height = h;
	}
	public void change(int bl,int h) {
		baseline = bl;
		height = h;
		System.out.println("밑변 = "+baseline);
		System.out.println("높이 = "+height);
	}
	public void tarea(int bl,int h) {
		result = bl*h*1/2;
		System.out.println("넓이 = "+result);
	}
	public void printres() {
		System.out.println("변경된 밑변과 높이 = "+baseline +" "+height);
		System.out.println("넓이 = "+result);
	}
}
