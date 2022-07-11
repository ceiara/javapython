package ex0707;

public class Person {
	
	private String name;
	
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String toString() {
		return "Person name = "+name;
	}
	
	public Person() {}
	public Person(String name) {
		//super(); // 생략 가능
		this.name = name; // 동일한 변수명 생략 불가
	}
}
	