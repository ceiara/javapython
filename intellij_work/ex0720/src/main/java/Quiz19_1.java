import java.util.Objects;

class Point1 {
    private int xPos;
    private int yPos;
    public Point1(int x, int y) {
        xPos = x;
        yPos = y;
    }
    @Override
    public boolean equals(Object o) {
        Point1 point1 = (Point1) o;
        return xPos == point1.xPos && yPos == point1.yPos;
    }

    @Override
    public int hashCode() {
        return Objects.hash(xPos, yPos);
    }
}

class Rectangle {
    public static Point1 upperLeft;
    public static Point1 lowerRight;
    public Rectangle(int x1, int y1, int x2, int y2) {
        upperLeft = new Point1(x1, y1);
        lowerRight = new Point1(x2, y2);
    }

}

public class Quiz19_1 {
    private static INum upperLeft;

    public static void main(String[] args) {
        Rectangle.upperLeft = new Point1(2, 7);
        Rectangle.lowerRight = new Point1(2, 7);
        System.out.println(Objects.equals(upperLeft, Rectangle.lowerRight));

        Point1 p1 = new Point1(4, 5);
        Point1 p2 = new Point1(4, 5);
        System.out.println(p1.equals(p2));
    }
}
