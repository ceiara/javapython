package member;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class Main {

    public static Map<String,MemberDTO> memberlist = new HashMap<>();

    private static AnnotationConfigApplicationContext ctx = null;

    public static void main(String[] args) throws Exception {
        MemberDTO md = new MemberDTO("aa@naver.com", "홍길동", "1234");
        memberlist.put("홍길동",md);

        MemberDTO md1 = new MemberDTO("bb@naver.com", "이길동", "1234");
        memberlist.put("이길동",md1);

        ctx = new AnnotationConfigApplicationContext(Config.class); // 객체 담는 통에 config 라는 class를 담아라
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // consol에서 읽어옴.

        System.out.println("1.회원가입 new aaa@naver.com 이름 1234");
        System.out.println("2.회원리스트 list");
        System.out.println("3.회원삭제 del 이름");
        System.out.println("4.종료 exit");

        while (true){
            String command = br.readLine(); // 한줄을 읽어서 command로 읽어 들어옴.
            if (command.equalsIgnoreCase("exit")) {
                System.out.println("프로그램 종료합니다");
                break;
            }
            else if (command.startsWith("new ")) {
                String name = command.split(" ")[1]; // 빈공백을 기준으로 자름.
                // 위의 코드가 없을 경우 새로운 정보 입력이 아니라 기존 정보가 수정된다.
                MemberDTO md2 = new MemberDTO("bb@naver.com", name, "1234");
                memberlist.put(name,md2);
                System.out.println("등록되었습니다.");
            }
            else if (command.equalsIgnoreCase("list")) {
                MemberDAO dao = ctx.getBean(MemberDAO.class);
                Collection<MemberDTO> collection = dao.selectAll();
                collection.forEach(m -> System.out.println(m));
            }
        }


//        System.out.println(memberlist);

    }
}
