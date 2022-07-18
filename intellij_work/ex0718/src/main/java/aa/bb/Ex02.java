package aa.bb;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Ex02 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        try{
            System.out.println("a ?");
            int a = scan.nextInt();
            System.out.println("b ?");
            int b = scan.nextInt();

            System.out.println("a/b = "+a/b);
            System.out.println("정상실행");

        }catch (ArithmeticException ae){
            System.out.println("20번째"+ae);
            ae.printStackTrace(); // 어디에서 예외가 발생하는지 표시
        }catch (InputMismatchException ime){
            System.out.println("22번째"+ime);
        }catch (Exception e) {
            System.out.println("모든 예외 처리"+e);
        }

        System.out.println("프로그램 종료됩니다.");
    }
}
