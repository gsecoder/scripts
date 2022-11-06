package main

import "fmt"

// ------------- 函数的基础 --------------
func testSum(a int, b int) int {
	sayName()
	c := a + b
	return c
}
func sayName()  {
	fmt.Println("这是一个加法函数")
}

// 函数的参数
func funcShort(x, y int) {
	fmt.Println("函数的参数中如果相邻变量的类型相同，则可以省略类型")
	fmt.Println(x , y)
}
func funcVariable(x int, y ... int) int {
	// 固定参数搭配可变参数使用时，可变参数要放在固定参数的后面
	sum := x
	for _, v := range y{
		sum = sum + v
	}
	return sum
}

// 函数的返回值
func funcReturnMulti(n, m int) (int, int)  {
	result1 := n - m
	result2 := n + m
	return result1, result2
}
func funcReturnRename(n, m int)(x, y int)  {
	x = n - m
	y = n + m
	return
}
func funcReturnNil(x string) []int {
	if x == "" {
		fmt.Println("nil")
	}
	return nil
}



func main() {
	// 函数的基础
	//fmt.Print(testSum(1, 2))
	//funcShort(1, 2)
	//fmt.Println(funcVariable(1, 10, 100, 1000))
	fmt.Println(funcReturnMulti(1, 2))
	fmt.Println(funcReturnRename(1, 2))
	fmt.Println(funcReturnNil(""))

}