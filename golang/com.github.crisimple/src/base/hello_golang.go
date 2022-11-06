package main // 声明 base 包，表明当前是一个可执行程序

/**
	这是多行注释
 */
import "fmt"

const (
	a, b = iota + 1, iota + 2
	c, d
	e, f
)

func printX()  { // 导入内置 fmt 包
	fmt.Println("Hello World!")  // 在终端打印 Hello World!
	fmt.Println("a: ", a)
	fmt.Println("b: ", b)
	fmt.Println("c: ", c)
	fmt.Println("d: ", d)
	fmt.Println("e: ", e)
	fmt.Println("f: ", f)
}
