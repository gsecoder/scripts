package mapper;

import org.apache.ibatis.session.SqlSession;
import org.junit.Test;
import pojo.Blog;
import util.IDUtil;
import util.MyBatisUtil;

import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;

/**
 * @Author crisimple
 * @File BlogTest
 * @Time 2021-04-10 11:58
 * @Description
 */
public class BlogTest {

    SqlSession sqlSession = MyBatisUtil.getSession();
    BlogMapper blogMapper = sqlSession.getMapper(BlogMapper.class);

    // 新增博客
    @Test
    public void addBlogTest(){

        Blog blog = new Blog();
        blog.setId(IDUtil.genId());
        blog.setTitle("MyBatis");
        blog.setAuthor("M");
        blog.setCreateTime(new Date());
        blog.setViews(99999);
        blogMapper.addBlog(blog);

        blog.setId(IDUtil.genId());
        blog.setTitle("Java");
        blogMapper.addBlog(blog);

        blog.setId(IDUtil.genId());
        blog.setTitle("Spring");
        blogMapper.addBlog(blog);

        blog.setId(IDUtil.genId());
        blog.setTitle("SQL");
        blogMapper.addBlog(blog);

        sqlSession.commit();
        sqlSession.close();
    }

    // IF语句
    @Test
    public void selectBlogIfTest(){

        HashMap<String, String> map = new HashMap<String, String>();
        map.put("title", "MyBatis");
        map.put("author", "M");

        List<Blog> blogList = blogMapper.selectBlogIf(map);
        System.out.println(blogList);

        sqlSession.close();
    }

    @Test
    public void updateBlogSetTest(){

        HashMap<String, String> map = new HashMap<String, String>();
        map.put("title", "动态SQL");
        map.put("author", "M");
        map.put("id", "23bcc81127d4445283cc57b7040318a4");
        blogMapper.updateBlogSet(map);

        sqlSession.commit();
        sqlSession.close();
    }

    @Test
    public void selectBlogChooseTest(){

        HashMap<String, String> map = new HashMap<String, String>();
        map.put("title", "Java");
        map.put("author", "M");
        map.put("views", "99999");

        List<Blog> blogList = blogMapper.selectBlogChoose(map);
        System.out.println(blogList);

        sqlSession.close();
    }

    @Test
    public void selectBlogForeachTest(){

        HashMap map = new HashMap();
        List<String> authors = new ArrayList<String>();
        authors.add("M1");
        authors.add("M2");
        authors.add("M3");
        authors.add("M4");
        map.put("authors", authors);

        List<Blog> blogList = blogMapper.selectBlogForeach(map);
        System.out.println(blogList);

        sqlSession.close();
    }
}
