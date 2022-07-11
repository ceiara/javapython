package ex0711;

public class Ex04 {
	Ex04() {
		BB b1 = new BB(); //2
		
		System.out.println(b1.toString()); //7, toString()생략 가능
		
		System.out.println("abc".equals(new String("abc")) );
		System.out.println("abc" == new String("abc"));
		
		String a = 12 +""; // 문자열과 더하면 문자열로 나타냄.
		String b = String.valueOf(12); // 굳이 함수 사용하지 않아도 결과는 동일
//		String c = 12; 문자열에 숫자를 담으려고 할 때 위의 같은 방법 사용
	}
	
	public static void main(String[] args) {
		new Ex04(); //1
	}
}
