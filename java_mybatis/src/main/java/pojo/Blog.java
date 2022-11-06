package pojo;
import lombok.Data;

import java.util.Date;

/**
 * @Author crisimple
 * @File Blog
 * @Time 2021-04-10 11:40
 * @Description
 */
@Data
public class Blog {

    private String id;
    private String title;
    private String author;
    private Date createTime;
    private int views;
}
