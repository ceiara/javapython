package org.example;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;

public class ChangePwdService {

    @Autowired(required = false)
    @Qualifier("memberdao1") // 자동 주입 가능한 bean이 두 개 이상일 때 명확하게 명시
    private MemberDao memberDao;

    public void chpwd(){
        memberDao.update();
    }
}
