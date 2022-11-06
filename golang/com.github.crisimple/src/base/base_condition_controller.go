package main

import "fmt"

func conditionIfElse()  {
	score := 90
	if score >=90 {
		fmt.Println("A")
	} else if score >= 80 {
		fmt.Println("B")
	} else {
		fmt.Println("C")
	}

	// if条件判断还有一种特殊的写法，在 if 表达式之前添加一个执行语句，再根据变量值进行判断
	if age := 25; age > 20{
		fmt.Println("A1")
	} else if age > 18{
		fmt.Println("B2")
	} else {
		fmt.Println("C3")
	}

}

func conditionFor() {
	for i := 0; i < 10; i++{
		fmt.Println(i)
	}

	// for循环的初始语句可以被忽略，但是初始语句后的分号必须要写
	j := 10
	for j > 0 {
		fmt.Println(j)
		j--
	}

	// for循环的初始语句可以被忽略，但是初始语句后的分号必须要写
	y := 0
	for ; y < 10; y++{
		fmt.Println(y)
	}
}


func conditionSwitchCase()  {
	finger := 3
	switch finger {
	case 1:
		fmt.Println("大拇指")
	case 2:
		fmt.Println("食指")
	case 3:
		fmt.Println("中指")
		// fallthrough 语法可以执行满足条件的case的下一个case
		fallthrough
	case 4:
		fmt.Println("无名指")
	case 5:
		fmt.Println("小拇指")
	default:
		fmt.Println("无效的输入！")
	}

	age := 20
	switch {
		case age < 20:
			fmt.Println("小孩")
		case age == 20:
			fmt.Println("成年了")
		case age > 20:
			fmt.Println("成年了")
	}

	switch n := 7; n {
	case 1, 3, 5, 7, 9:
		fmt.Println("奇数")
	case 2, 4, 6, 8:
		fmt.Println("偶数")
	default:
		fmt.Println(n)
	}

	s := "a"
	switch {
	case "a" == s:
		fmt.Println("a")
		fallthrough
	case "b" == s:
		fmt.Println("b")
	case "c" == s:
		fmt.Println("c")
	default:
		fmt.Println("...")
	}
}

func conditionGoto()  {
	var breakFlag bool
	for i := 0; i < 10; i++ {
		for j := 0; j < 10; j++ {
			if j == 2 {
				// 设置退出标签
				breakFlag = true
				break
			}
			fmt.Printf("%v-%v\n", i, j)
		}
		// 外层for循环判断
		if breakFlag {
			break
		}
	}
}

func conditionGoto2()  {
	for i := 0; i < 10; i++ {
		for j := 0; j < 10; j++ {
			if j == 2 {
				// 设置退出标签
				breakFlag()
			}
			fmt.Printf("%v-%v\n", i, j)
		}
	}
}
func breakFlag()  {
	fmt.Println("结束for循环")
}


func conditionBreak() {
BREAKDEMO1:
	for i := 0; i < 10; i++ {
		for j := 0; j < 10; j++ {
			if j == 2 {
				break BREAKDEMO1
			}
			fmt.Printf("%v-%v\n", i, j)
		}
	}
	fmt.Println("...")
}

func conditionContinue()  {
forloop:
	for i := 0; i < 5; i++ {
		// forloop2:
		for j := 0; j < 5; j++ {
			if i == 2 && j == 2 {
				continue forloop
			}
			fmt.Printf("%v-%v\n", i, j)
		}
	}
}

//func main() {
//	//conditionIfElse()
//	//conditionFor()
//	//conditionSwitchCase()
//	//conditionGoto()
//	//conditionGoto2()
//	//conditionBreak()
//	conditionContinue()
//}