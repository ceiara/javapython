package ex0708;

public class Accumulator {

	class Add {
		int i = 0;
		int sum = 0;
		public Add(int i, int sum) {
			sum += i;
		}
		public showResult() {
			System.out.println();
		}
	}
	
	public static void main(String[] args) {
		Add add = new Add();
		for(int i=0;i<10;i++) {
			Accumulator.add(i);
			
		Accumulator.showResult();
		}
	}
}
