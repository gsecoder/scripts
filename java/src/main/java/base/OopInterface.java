package base;

/**
 * @file base.OopInterface
 * @author sf
 * @date 2020/8/21 6:17 下午
 * @description 引用类型：接口
 */

public class OopInterface {

public static void main(String[] args) {
	// main 方法
}
}

/**
 * 使用 interface 定义接口（类比于类的 class 关键词）
 */
interface UserService {

/**
 * 接口中的常量不用关键词（final、public、static）修饰，
 * 是因为其默认就加了该关键词的修饰了，加上了是置灰状态，生效不高亮
 */
int AGE = 120;
final int TALL = 180;
public static String name = "XiaoA";

/**
 * 接口中所有定义的方法都是抽象的，但是不用加修饰符（public abstract）
 *
 * @param name
 */
void addPerson(String name);

/**
 * 删除用户
 *
 * @param name
 */
void deletePerson(String name);

/**
 * 更新用户
 *
 * @param name
 * @param sex
 */
public abstract void updatePerson(String name, char sex);

/**
 * 查询用户
 *
 * @param name
 */
public abstract void selectPerson(String name);
	
}

/**
 * 时间服务类
 */
interface TimerService {
/**
 * 计时器
 */
void timer();
}

/**
 * 特别注意：实现了接口的类，就需要继承所有类的方法；不然继承的类就会报错或者是转成抽象类
 * 类可以实现接口implements 按口
 * 多继承~利用接口实现多继承
 * abstract class base.UserServiceImpl implements base.UserService, base.TimerService {
 * <p>
 * }
 */

class UserServiceImpl implements UserService, TimerService {
@Override
public void addPerson(String name) {
	
}

@Override
public void deletePerson(String name) {
	
}

@Override
public void updatePerson(String name, char sex) {
	
}

@Override
public void selectPerson(String name) {
	
}

@Override
public void timer() {
	
}
}