package ex0711;

public class Quiz11_2 {

	public static void main(String[] args) {
		StringBuilder stbuf = new StringBuilder("990925-1012999");
		
		stbuf.replace(6, 7, " ");
		System.out.println(stbuf.toString());
	}
}
