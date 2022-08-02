package org.example;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
    private static AnnotationConfigApplicationContext acac = null; // acac가 main 함수에 있으므로 class 변수로 만들어 listCommand도 사용할 수 있도록 함
    public static void listCommand() {
        MemberService memberService = acac.getBean(MemberService.class);
        memberService.list();
    }

    public static void newCommand(MemberDto dto) { // MemberDto를 dto로 선언
        MemberService memberService = acac.getBean(MemberService.class);
        try {
            memberService.resist(dto);
        }catch (Exception e) {
            System.out.println("email duplicated. can't put in");
        }
    }

    private static void updatecommand(String email, String oldpwd, String newpwd) {
        MemberService memberService = acac.getBean(MemberService.class);
        try {
            memberService.updatepwd(email, oldpwd, newpwd);
        }catch (Exception e) {
            System.out.println();
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 사용자가 입력하도록 함.
        acac = new AnnotationConfigApplicationContext(ClassConfig.class); // 스프링 객체 담는 통
        try {
            while (true) {
                System.out.println("1.list 2.new aa@naver.com 3.update 4.exit");
                String cmd = br.readLine(); // 입력받음
                if(cmd.equalsIgnoreCase("list")){ // 대소문자 상관없이 들어옴
                    listCommand();
                }
                else if(cmd.startsWith("new")){
                    try {
                        String email = cmd.split(" ")[1];
                        String name = cmd.split(" ")[2];
                        String pwd = cmd.split(" ")[3];
                        MemberDto md = new MemberDto(name, email, pwd);
                        newCommand(md);
                    } catch (IndexOutOfBoundsException ie){ // IndexOutOfBoundsException: list형 객체에서 선언되지 않은 요소를 get 할 경우 발생
                        System.out.println("new aa@naver.com Sara 1234 \n이렇게 입력하세요.");
                    }

                } else if (cmd.startsWith("update")) {
                    // update aa@naver.com 1234 5678
                    try {
                        String email = cmd.split(" ")[1];
                        String oldpwd = cmd.split(" ")[2];
                        String newpwd = cmd.split(" ")[3];
                        updatecommand(email, oldpwd, newpwd);
                    }catch (Exception e){
                        System.out.println("update aa@naver.com Sara 1234 \n이렇게 입력하세요.");
                        System.out.println(e.toString());
                    }
                } else if (cmd.equalsIgnoreCase("exit")) {
                    System.out.println("종료됩니다.");
                    break;
                }
            }
        }catch (Exception e) { //
            e.printStackTrace();
        }
        finally { // spring container을 무너뜨림, finally는 거의 무조건적으로 들어감
            acac.close();
        }
    }
}