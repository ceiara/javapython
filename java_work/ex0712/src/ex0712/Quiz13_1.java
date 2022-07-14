package ex0712;

public class Quiz13_1 {

	public static int [] ary = {6,45,8,23,4,78,5};
	
	public static int minValue(int[] arr) {
		int min = ary[0];
		for(int i=0;i<ary.length;i++) {
			if(min<ary[0]) {
				min = ary[0];
			}
		}
		return min;
	}
	public static int maxValue(int[] arr) {
		int max = ary[0];
		for(int temp:ary) {
			if(max < temp) {
				max = temp;
			}
		}
		return max;
	}
			
	public static void main(String[] args) {
		int min = minValue(ary);
		int max = maxValue(ary);
		
		System.out.println("최솟값 = "+min);
		System.out.println("최댓값 = "+max);
	}
}