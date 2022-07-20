class Person implements Cloneable{
    String name; // only String형만 자동으로 깊은 복사
    int age; // 자동으로 깊은 복사
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
    @Override
    protected Object clone() throws CloneNotSupportedException {
        Person p1 = (Person) super.clone();
        p1.name = new String(name);
        return p1;
    }
}

public class Ex03 {
    public static void main(String[] args) throws CloneNotSupportedException {
        Person p1 = new Person("홍길동", 50);
        Person p2 = (Person) p1.clone();
        System.out.println(p1);
        System.out.println(p2);

        p1.name = "김길동";
        p1.age = 100;
        System.out.println(p1);
        System.out.println(p2);
    }
}
