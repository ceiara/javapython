package com.dip.myapp.member;

import java.sql.PreparedStatement;
import java.time.LocalDate;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

@Repository
public class MemberDao {

	@Autowired
	private JdbcTemplate jdbcTempalte;

	public void insert(MemberDto memberDto) {
//		jdbcTempalte.update(new PreparedStatementCreator() {
//			@Override
//			public PreparedStatement createPreparedStatement(Connection con) throws SQLException {
//				// TODO Auto-generated method stub
//				return null;
//			}
//		});
		jdbcTempalte.update((con)->{
			PreparedStatement pstmt = 
					con.prepareStatement("insert into member"
							+ "(EMAIL, PASSWORD, NAME, REGDATE) "
							+ "values (?,?,?,?)");
			pstmt.setString(1, memberDto.getEmail());
			pstmt.setString(2, memberDto.getPassword());
			pstmt.setString(3, memberDto.getName());
			pstmt.setString(4, LocalDate.now().toString());
			return pstmt;
		});
	}
}
