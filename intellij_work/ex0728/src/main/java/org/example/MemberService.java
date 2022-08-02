package org.example;

import org.springframework.beans.factory.annotation.Autowired;

public class MemberService {

    @Autowired
    private MemberDao memberDao;

    // 저장
    public void regist(){
        memberDao.insert();
    }
    // 보기
    public void getall(){
        memberDao.selectall();
    }

    // 삭제
    // 변경

}
