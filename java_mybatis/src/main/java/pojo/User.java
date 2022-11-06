package pojo;

/**
 * @Author crisimple
 * @File User
 * @Time 2021-04-04 16:08
 * @Description
 */
public class User {

    /**
     * 用户ID
     */
    private Integer id;
    /**
     * 用户姓名
     */
    private String username;
    /**
     * 用户密码
     */
    private String password;

    /**
     * 无参构造器
     */
    public User() {
    }

    /**
     * 有参构造器
     * @param id
     * @param username
     * @param password
     */
    public User(int id, String username, String password) {
        this.id = id;
        this.username = username;
        this.password = password;
    }

    /**
     * Get、Set方法
     * @return
     */
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    /**
     * toString
     * @return
     */
    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", username='" + username + '\'' +
                ", password='" + password + '\'' +
                '}';
    }
}
