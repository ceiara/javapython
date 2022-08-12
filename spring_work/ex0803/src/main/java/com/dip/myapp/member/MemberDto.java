package com.dip.myapp.member;

public class MemberDto {

	private int id;
	private String email;
	private String name;
	private String password;
	private String regdata;

//	기본생성자
	public MemberDto() {}

	public MemberDto(int id, String email, String name, String password, String regdata) {
		super();
		this.id = id;
		this.email = email;
		this.name = name;
		this.password = password;
		this.regdata = regdata;
	}

	@Override
	public String toString() {
		return "MemberDto [id=" + id + ", email=" + email + ", name=" + name + ", password=" + password + ", regdata=" + regdata
				+ "]";
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getPassword() {
		return password;
	}

	public void setPwd(String pwd) {
		this.password = pwd;
	}

	public String getRegdata() {
		return regdata;
	}

	public void setRegdata(String regdata) {
		this.regdata = regdata;
	}

}
