package ex0707;

import zoo.Duck;

public class Ex02 {
	Ex02(){
		zoo.Dog dog = new zoo.Dog();
		zoo.Cat cat = new zoo.Cat();
		Duck duck = new Duck();
		sound(dog, cat, duck);
	}
	
	public void sound(zoo.Dog dog,zoo.Cat cat,Duck duck) {
		dog.sound();
		cat.sound();
		duck.sound();
	}
	
	public static void main(String[] args) {
		new Ex02();
		// new는 생성자가 호출되면서 heap 영역으로 올라가게 됨.
		// static 프로그램이 끝날 때까지 항상 상주
	}
}
