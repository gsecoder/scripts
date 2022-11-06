package main

import (
	"bufio"
	"fmt"
	"os"
)

func fmtScan()  {
	// fmt.Scan
	var name string
	var age int
	fmt.Println("请输入用户名：")
	// 当使用Scan时，会提示用户输入
	// 用户输入完成之后，会得到两个值：count,用户输入了几个值；err，用输入错误则是错误信息
	// 特别说明：fmt.Scan 要求输入两个值，必须输入两个，否则他会一直等待。
	_, err := fmt.Scan(&name, &age)
	if err == nil {
		fmt.Println(name, age)
	} else {
		fmt.Println("用户输入数据错误", err)
	}
}

func fmtScanln()  {
	// fmt.Scanln
	// 特别说明：fmt.Scanln 等待回车
	var name1 string
	var age1 int
	fmt.Print("请输入用户名：")
	// 当使用ScanIn时，会提示用户输入
	// 用户输入完成之后，会得到两个值：count,用户输入了几个值；err，用输入错误则是错误信息
	count, err := fmt.Scanln(&name1, &age1)
	fmt.Println(count, err)
	fmt.Println(name1, age1)
}


func fmtScanf() {
	var name string
	var age int

	fmt.Print("请输入用户名\n")
	_, _ = fmt.Scanf("我叫%s，今年%d岁", name, age)
	fmt.Println(name, age)
}


func readLine()  {
	// line，从stdin中读取一行的数据（字节集合 -> 转化成为字符串）;reader默认一次能4096个字节（4096/3)
	// 		1. 一次性读完，isPrefix=false
	//		2. 先读一部分，isPrefix=true，再去读取isPrefix=false
	reader := bufio.NewReader(os.Stdin)
	line, _, _ := reader.ReadLine()
	data := string(line)
	fmt.Println(data)
}



func main1()  {
	//fmtScan()
	//fmtScanln()
	//fmtScanf()
	readLine()
}
