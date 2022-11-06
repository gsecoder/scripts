package mapper;

import pojo.User;
import java.util.List;
import java.util.Map;

public interface UserMapper {

    /**
     * 查询全部的用户
      * @return
     */
    List<User> selectUser();
    
    // 根据参数条件查询用户
    User selectParamsUser(int id);
    
    // 模糊查询LIKE
    List<User> selectLikeUser(String name);
    
    // 万能的map
    Map<String, Object> selectMapUser(Map<String, Object> map);
    
    // 分页查询（使用LIMIT实现在SQL中分页）
    List<User> selectLimitUser(Map<String, Integer> map);
    
    // 分页查询2（使用RowBounds在Java层面实现分页）
    List<User> selectRowBoundsUser();
    
    // 增加新用户
    int addUser(User user);
    
    // 更新用户
    int updateUser(User user);
    
    // 删除用户
    int deleteUser(int id);
}
