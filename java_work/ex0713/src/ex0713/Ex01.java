package ex0713;

public class Ex01 {

	public static int [] ary = {10,20,5,6,9,33};
	
	public static int minValue(int[] arr) {
		int min = ary[0];
		for(int i=0; i<ary.length;i++) { 
			if(min > ary[i]) {
				min = ary[i];
			}
		}
		return min; // 0번째 i(10)이 반복되는 다음 수와 비교했을 때 값이 더 크면 비교한 더 작은 값으로 바꾼다.
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
