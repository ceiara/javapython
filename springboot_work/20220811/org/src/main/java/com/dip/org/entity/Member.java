package com.dip.org.entity;

import lombok.*;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Getter
@Setter
@AllArgsConstructor
@RequiredArgsConstructor
@ToString
public class Member {
    @Id
    @GeneratedValue(strategy = GenerationType.TABLE)
    @Column(name = "id", nullable = false)
    private Long id;

//    private String password;
    private String email;
    private String remark;
    private String gender;
    private LocalDateTime regdate;

    private String password;
    private String name;
}
