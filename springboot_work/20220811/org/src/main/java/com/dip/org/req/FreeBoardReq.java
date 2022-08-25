package com.dip.org.req;

// 유효성검사 validation
// form 저장버튼을 눌렀을 시 글 내용, 제목이 없을때 다시 입력받도록 유도하는 기능

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import javax.validation.constraints.NotEmpty;
import java.time.LocalDateTime;

@Getter
@Setter
@ToString
public class FreeBoardReq {
    private Long id;

    @NotEmpty
    private String title;
    @NotEmpty
    private String content;

    private String filename;
    private int hits;

    private LocalDateTime regdate;
}
