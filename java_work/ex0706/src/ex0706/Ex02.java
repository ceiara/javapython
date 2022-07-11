package ex0706;

import myclass.ZZZ; // 다른 package에 있을때 import 사용.

public class Ex02 {
	public static void main(String[] args) {
		AAA aaa = new AAA();
		aaa.doA();
		
		ZZZ zzz = new ZZZ();
		zzz.doA();
	}
}
