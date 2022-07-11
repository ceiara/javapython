package zoo;

public class Circle {

	int xPos, yPos, radius;
	public Circle(int x, int y, int r) {
		xPos = x;
		yPos = y;
		radius = r;
	}
	public void showPointInfo() {
		System.out.println("[" + xPos + "," + yPos + "]");
	}
	public void showradiusInfo() {
		System.out.println("r = "+radius);
	}
	public void showCircleInfo() {
		System.out.println("[" + xPos + "," + yPos + "] "+"r = "+radius);
	}
}
