package com.dip.org.repository;

import com.dip.org.entity.FreeBoard;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

@Repository
public interface FreeBoardRepository extends JpaRepository<FreeBoard,Long> {

    //    @Query(value = "delete from free_board_tail f where f.board_id=?1",nativeQuery = true)
//    int deleteAllByBoard_Id(long board_id);

//    void deleteAllByBoard_id(Long id);
}