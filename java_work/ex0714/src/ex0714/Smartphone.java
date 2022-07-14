package ex0714;

public class Smartphone extends Phone {

	private String ver;
	
	Smartphone(String num,String ver) {
		super(num);
		this.ver = ver;
	}

	@Override
	public String toString() {
		return "Smartphone [ver=" + ver + "]";
	}
	
	public static void main(String[] args) {
		Smartphone sp = new Smartphone("1234-1234", "0.5");
		sp.doPrint();
		System.out.println(sp);
	}
	
}
