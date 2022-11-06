package aop;

/**
 * @Author crisimple
 * @File AopServiceImpl
 * @Time 2021-04-03 18:01
 * @Description
 */
public class AopServiceImpl implements AopService{

    @Override
    public void add() {
        System.out.println("增加用户");
    }

    @Override
    public void delete() {
        System.out.println("删除用户");
    }

    @Override
    public void update() {
        System.out.println("更新用户");
    }

    @Override
    public void select() {
        System.out.println("查找用户");
    }
}
