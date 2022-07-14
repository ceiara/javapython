package ex0712;

public class Ex04 {

	public static void main(String[] args) {
		AA[] ar = new AA[5]; // ar 공간만 5개 만들어준 것, null
		
		System.out.println(ar[0]);
		System.out.println(ar[1]);
		
		System.out.println(ar.length);
		
		ar[0] = new AA("홍길동");
		System.out.println(ar[0]);
	}
}
