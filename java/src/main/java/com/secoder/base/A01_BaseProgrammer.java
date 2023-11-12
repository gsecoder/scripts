package com.secoder.base;

/**
 * ********** 类的说明部分 **********
 *
 * @param '参数名'
 * @author 作者名
 * @version 版本号
 * @return 返回值情况
 * @throws '异常抛出情况'
 * @since 指明需要的jdk版本
 */
class JavaDoc {
String name;

/**
 * ********** 方法的说明部分 **********
 *
 * @param name
 * @return name
 * @throws Exception
 */
    public String test(String name) throws Exception {
        return name;
    }
}

public class A01_BaseProgrammer {
    BaseKeyword bk = new BaseKeyword();
}

/**
 * 关键字
 */
class BaseKeyword {
    public static void main(String[] args){
        System.out.println("关键字");
    }
}