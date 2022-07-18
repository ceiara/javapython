package ex0714;

public class Quiz15 {

static class Box {
	public void simpleWrap() {
		System.out.println("Simple Wrapping");
	}
}

static class PaperBox extends Box {
	public void paperWrap() {
		System.out.println("Paper Wrapping");
	}
}

static class GoldPaterBox extends PaperBox {
	public void goldWrap() {
		System.out.println("Gold Wrapping");
	}
}

class Wrapping {
	public static void main(String[] args) {
		Box box1 = new Box();
		PaperBox box2 = new PaperBox();
		GoldPaterBox box3 = new GoldPaterBox();
		
		wrapBox(box1);
		wrapBox(box2);
		wrapBox(box3);
	}
	
	public static void wrapBox(Box box) {
		if (box instanceof GoldPaterBox) {
			((GoldPaterBox)box).paperWrap();
		}
		else if (box instanceof PaperBox) {
			((PaperBox)box).paperWrap();
		}
		else {
			box.simpleWrap();
		}
	}
}
}
