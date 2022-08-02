package org.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class MemberService {

	@Autowired
	private MemberDao memberDao;
	
	public void newMember(MemberDto memberDto) {
		// 해당되는 email이 존재유무 확인
		// 없으면 data 추가
		// 있으면 data 넣을 수 없다 중복
		//memberDao.getSelectByEmail(memberDto.getEmail());
		
		memberDao.insert(memberDto);
	}
	
	public void printMember() {
		memberDao.selectall().forEach(m -> System.out.println(m));
	}

}
