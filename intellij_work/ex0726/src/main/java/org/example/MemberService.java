package org.example;

import org.springframework.beans.factory.annotation.Autowired;

public class MemberService {
    @Autowired
    private MemberDAO memberDAO; // MemberDAO는 class memberDAO를 가지고 있다.
    @Autowired
    private MemberPrinter memberPrinter;

//    public void setMemberPrinter(MemberPrinter memberPrinter) {
//        this.memberPrinter = memberPrinter;
//    }
//
//    public MemberService(){}
//    // 생성자에 의한
//    public MemberService(MemberDAO memberDAO) {
//        this.memberDAO = memberDAO;
//    }
//    // setter에 의한
//    public void setMemberDAO(MemberDAO memberDAO) {
//        this.memberDAO = memberDAO;
//    }

    public void list() {
        memberDAO.selectAll();
    }

    // datamap 안에 같은 이메일이 있으면 저정할 수 없다
    // 아니면 저장을 해야 한다.
    public void resist(MemberDto dto) throws Exception {
//        System.out.println(dto);
        String result = memberDAO.getSelectByEmail(dto.getEmail()); // data 안에 email 존재 여부에 따라 예외처리
        if(result.equals("have"))
            throw new Exception();
        else
            memberDAO.insert(dto);
    }

    public void updatepwd(String email, String oldpwd, String newpwd) throws Exception {
        String result = memberDAO.changePwd(newpwd);
        if (result.equals("no change"))
            throw new Exception();
        else
            memberDAO.insert(newpwd);
    }
}
