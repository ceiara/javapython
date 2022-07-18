package aa.bb;

class PA{
    public void showInfo(){
        System.out.println("PA 메서드입니다.");
    }
}
class CA1 extends PA{
    @Override
    public void showInfo() {
        super.showInfo();
        System.out.println("c1 메서드입니다.\n");
    }
    @Override
    public String toString() {
        return "CA1";
    }
}
class CA2 extends PA{
    @Override
    public void showInfo() {
        super.showInfo();
        System.out.println("c2 메서드입니다.\n");
    }
    @Override
    public String toString() {
        return "CA2";
    }
}
public class Main {
    public static void main(String[] args) {
        PA pa[] = new PA[5];
        System.out.println("pa[0]"+pa[0]);

        pa[0] = new CA1();
        System.out.println("pa[0]"+pa[0]);
        pa[1] = new CA2();
        System.out.println("pa[1]"+pa[0]);

        pa[0].showInfo();
        pa[1].showInfo();

        pa[2] = new CA1();

        try {
            CA1 ca1 = (CA1) pa[2]; // 강제형변환
            CA2 ca2 = (CA2) pa[2]; // pa <-> CA1, pa <-> CA2, CA1<-> CA2(X)

            System.out.println(ca1);
            // System.out.println(ca2);  // error
            System.out.println("여기까지 정상실행");
        }catch (Exception e){
            System.out.println("에러발생 무시..."+e);
            // 예외가 발생했을 때 실행
        }

        System.out.println("프로그램 종료합니다.");

    }
}
