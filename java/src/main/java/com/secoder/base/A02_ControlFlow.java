package com.secoder.base; /**
 * @file A02_ControlFlow
 * @author secoder
 * @date 2022/8/29 16:57
 * @description 流程控制
 */

import java.util.Scanner;

public class A02_ControlFlow {

}

/**
 * 顺序结构
 */
class SequentialStructure {

    public static void main(String[] args) {
        int num1 = 12;                      // 1.执行语句1
        // 定义成员变量时采用合法的前向引用
        int num2 = num1 + 2;                // 2.执行语句2
    }
}


/**
 * 分支选择if...else..
 */
class BranchSelectionIfElse {
    // 分支选择if...else..
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("if单选泽请输入");
        String s = scanner.nextLine();
        System.out.println("if双选择请输入");
        int score = scanner.nextInt();

        /*
         * if 选择结构
         */
        // if 单选择结构
        if(s.equals("com.secoder.base.Hello")) {
            System.out.println(s);
        }
        System.out.println("End");

        // if 双选择结构
        if(score >= 60) {
            System.out.println("成绩及格了");
        } else {
            System.out.println("成绩不及格");
        }
        System.out.println("End");

        // if 多选择结构
        if(score < 60) {
            System.out.println("不及格");
        } else if(60 <= score && score < 70) {
            System.out.println("及格");
        } else if(70 <= score && score < 90) {
            System.out.println("良好");
        } else if(90 <= score && score <= 100) {
            System.out.println("优秀");
        } else {
            System.out.println("输入成绩不正确");
        }
        scanner.close();
    }
}

/**
 * 分支选择switch...case..
 */
class BranchSelectionSwitchCase {
    // 分支选择switch...case...
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int score = scanner.nextInt();

        /*
         * switch 多分支选择，JDK7 以后支持字符串的比较
         * */
        switch (score) {
            case 'A':
                System.out.println("优秀");
                break;
            case 'B':
                System.out.println("良好");
                break;
            case 'C':
                System.out.println("及格");
                break;
            case 'D':
                System.out.println("再接再厉");
                break;
            default:
                System.out.println("默认输出");
        }
    }
}

/**
 * 循环结构：
 *  1. while循环
 *  2. do...while 循环
 *  3. for 循环
 */
class LoopStruct {

    public static void main(String[] args) {
        /*
         * while循环
         * */
        int num = 0;
        int num1 = 0;
        int sum = 0;
        while (num1 <= 10) {
            sum += num;
            num1++;
        }
        System.out.println("sum = " + sum);
        System.out.println("===== 华丽的分割线1 =====");
        while (num < 0) {
            System.out.println("num: " + num);
        }
        System.out.println("===== 华丽的分割线2 =====");

        /*
         * do...while 循环
         * */
        do {
            num++;
            System.out.println("num: " + num);
        } while (num < 0);


        /*
         * for 循环
         * 快捷生成：100.for
         * */
        System.out.println("===== for 循环分割线 =====");
        for (int i = 1; i <= 100; i++) {
            System.out.println(i);
        }
        System.out.println("===== for 循环结束 =====");


        /*
         * 用于数组的增强型 for 循环
         * JDK5 引入的
         * */
        int[] nums = {10, 20, 30, 40, 50};
        for (int x : nums) {
            System.out.println("x: " + x);
        }
    }
}


/**
 * 特殊流程控制break
 */
class SpecialControlFlowBreak{
    public static void main(String[] args) {
        for (int i=0; i<10; i++){
            if (i==3){
                break;
            }
            System.out.print("i=" + i + "\n");
        }
        System.out.print("Loop Break~~；后面的循环不会再执行！");
    }
}

/**
 * 特殊控制流程continue
 */
class SpecialControlFlowContinue{
    public static void main(String[] args) {
        for (int i=0; i<10; i++){
            if (i==3){
                continue;
            }
            System.out.print("i=" + i + "\n");
        }
        System.out.print("Loop Continue~~；后面的循环会继续执行！");
    }
}
