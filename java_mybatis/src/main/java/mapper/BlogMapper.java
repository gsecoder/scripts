package mapper;

import pojo.Blog;

import java.util.List;
import java.util.Map;

public interface BlogMapper {

    // 新增博客
    int addBlog(Blog blog);

    // IF语句（配合WHERE使用）
    //（需求：根据作者名字和博客名字来查询博客！如果作者名字为空，那么只根据博客名字查询，反之，则根据作者名来查询）
    List<Blog> selectBlogIf(Map map);

    // 更新博客（SET关键词使用）
    int updateBlogSet(Map map);

    // choose语句
    List<Blog> selectBlogChoose(Map map);

    // foreach
    List<Blog> selectBlogForeach(Map map);
}
