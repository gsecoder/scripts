package mapper;

import org.apache.ibatis.annotations.Param;
import pojo.User;

public interface SQLCacheMapper {

    // 根据用户ID查询用户
    User selectUserById(@Param("id") int id);
}
