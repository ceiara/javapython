package ex0714;

class Super{
	
}
class Sub extends Super {
	
}

public class Ex05 {

	public static void main(String[] args) {
		Super super1 = new Sub();
		Sub sub1 = (Sub) super1; //부모를 강제로 형변환하면 자식에 넣을 수 있다 
		
	}
}
