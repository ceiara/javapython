package org.example;

import java.util.HashMap;

public class MemberDAO {
    public static HashMap<String,MemberDto> data = new HashMap<>();

    public void selectAll() {
//        System.out.println(this);
        System.out.println("[data 출력]");
        if (data.size() == 0) System.out.println("data 내용없음");
        data.values().forEach(memberDto -> System.out.println(memberDto)); // value를 하나씩 출력
        System.out.println(); // 줄바꿈
    }

    public void insert(MemberDto dto) {
//        System.out.println(this);
        data.put(dto.getEmail(),dto); // (key, value) key를 주면 value 나옴
    }

    public String getSelectByEmail(String email) {
        MemberDto dto = data.get(email);
        if (dto != null)
            return "have";
        else
            return "don't have";
    }

    public String changePwd(String newpwd) {
        MemberDto dto = data.get(newpwd);
        if (dto != newpwd) {
            return "no change";
        } else
            return "change";
    }

    public void insert(String newpwd) {

    }
}
