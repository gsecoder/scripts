package main

import (
	"fmt"
	"math/rand"
	"sort"
	"time"
)

// 初始化数组时可以使用初始化列表来设置数组元素的值
func initArray1()  {
	var testArray [3]int                        //数组会初始化为int类型的零值
	var numArray = [3]int{1, 2}                 //使用指定的初始值完成初始化
	var cityArray = [3]string{"北京", "上海", "深圳"} //使用指定的初始值完成初始化
	fmt.Println(testArray)                      //[0 0 0]
	fmt.Println(numArray)                       //[1 2 0]
	fmt.Println(cityArray)                      //[北京 上海 深圳]
}

// 按照上面的方法每次都要确保提供的初始值和数组长度一致，一般情况下我们可以让编译器根据初始值的个数自行推断数组的长度
func initArray2()  {
	var testArray [3]int
	var numArray = [...]int{1, 2}
	var cityArray = [...]string{"北京", "上海", "深圳"}
	fmt.Println(testArray)                          //[0 0 0]
	fmt.Println(numArray)                           //[1 2]
	fmt.Printf("type of numArray:%T\n", numArray)   //type of numArray:[2]int
	fmt.Println(cityArray)                          //[北京 上海 深圳]
	fmt.Printf("type of cityArray:%T\n", cityArray) //type of cityArray:[3]string
}

// 可以使用指定索引值的方式来初始化数组
func initArray3()  {
	a := [...]int{1: 1, 3: 5}
	fmt.Println(a)                  // [0 1 0 5]
	fmt.Printf("type of a:%T\n", a) //type of a:[4]int
}


// 遍历数组
func indexArray()  {
	// 方法一：for...循环遍历
	var a = [...]string{"北京", "上海", "广州", "深圳"}
	for i := 0; i < len(a); i++ {
		fmt.Println(a[i])
	}

	// 方法二：for range遍历
	for index, value := range a {
		fmt.Println(index, "-", value)
	}
}


// 多维数组
func multiArray()  {
	// 二位数组的定义
	// 多维数组只有第一层可以使用...来让编译器推导数组长度
	a := [...][2]string{
		{"北京", "上海"},
		{"广州", "深圳"},
		{"西安", "宝鸡"},
	}
	fmt.Println(a)
	fmt.Println(a[2][0])
	fmt.Println("---------------")

	// 二维数组的遍历
	for _, v1 := range a {
		for _, v2 := range v1 {
			fmt.Println(v2, "\t")
		}
		fmt.Println()
	}
}


// 数组是值类型，赋值和传参会复制整个数组。因此改变副本的值，不会改变本身的值
func modifyArray1(x [3]int)  {
	x[0] = 100
}
func modifyArray2(x [3][2]int)  {
	x[2][0] = 100
}
func copyArray()  {
	a := [3]int{10, 20, 30}
	modifyArray1(a)	 // 在modify中修改的是a的副本x
	fmt.Println(a)	// [10 20 30]

	b := [3][2]int{
		{1, 1},
		{1, 1},
		{1, 1},
	}
	modifyArray2(b)		// 在modify中修改的是b的副本x
	fmt.Println(b)		// [[1 1] [1 1] [1 1]]
}



// ----------------------------- 切片 ------------------------
// 因为数组的长度是固定的并且数组长度属于类型的一部分，所以数组有很多的局限性
// 这个求和函数只能接受[3]int类型，其他的都不支持
func arraySum(x [3]int) int {
	sum := 0
	for _, v := range x{
		sum += v
	}
	return sum
}

// 切片的简单了解
func knowSection()  {
	// 声明切片类型
	var stringA []string               // 声明一个字符串切片
	var intB = []int{}                 // 声明一个整型切片并初始化
	var booleanC = []bool{false, true} // 声明一个布尔切片并初始化
	var _ = []bool{false, true}        // 声明一个布尔切片并初始化
	fmt.Println(stringA)
	fmt.Println(intB)
	fmt.Println(booleanC)
	fmt.Println(stringA == nil)
	fmt.Println(intB == nil)
	fmt.Println(booleanC == nil)
	//fmt.Println(booleanC == booleanD)		切片是引用类型，不支持直接比较，只能和nil比较

	// 切片的长度
	fmt.Println("stringA len is: ", len(stringA))
	fmt.Println("intB len is: ", len(intB))
	fmt.Println("booleanC len is: ", len(booleanC))

	// 切片的容量
	fmt.Println("stringA cap is: ", cap(stringA))
	fmt.Println("intB cap is: ", cap(intB))
	fmt.Println("booleanC cap is: ", cap(booleanC))

}

// 基于数组创建切片表达式
func SectionExpress()  {
	// 简单切片表达式
	a := [5]int{1, 2, 3, 4, 5}
	fmt.Println(a[2: ])
	fmt.Println(a[:3])
	fmt.Println(a[:])
	s := a[1: 3]
	fmt.Printf("s:%v\n len(s):%v\n cap(s):%v\n", s, len(s), cap(s))


	// 完整切片
	// 完整切片表达式需要满足的条件是0 <= low <= high <= max <= cap(a)，其他条件和简单切片表达式相同。
	b := [5]int{1, 2, 3, 4, 5}
	t := b[1:3:5]
	fmt.Printf("t:%v\n len(t)%v\n cap(t)%v", t, len(t), cap(t))
}
// 使用make()函数动态构造切片
func SectionMake()  {
	a := make([]int, 3, 10)
	fmt.Println("a: ", a)
	fmt.Println("len(a): ", len(a))
	fmt.Println("cap(a): ", cap(a))
}
// --------------------------- 切片的操作 ------------------------------
// 切片的比较
func sectionCompare()  {
	var s1 []int
	fmt.Printf("s1:%v\n len(s1):%v\n cap(s1):%v\n", s1, len(s1), cap(s1))
	s2 := []int{}
	fmt.Printf("s2:%v\n len(s2):%v\n cap(s2):%v\n\n", s2, len(s2), cap(s2))
	s3 := make([]int, 0)
	fmt.Printf("s3:%v\n len(s3):%v\n cap(s3):%v\n\n", s3, len(s3), cap(s3))
	fmt.Println(s3 == nil)
}
// 切片的赋值&拷贝
func sectionAssignmentCopy()  {
	// 切片的赋值
	s1 := make([]int, 3)
	s2 := s1	// s1直接赋值给s2，s2和s1共享一个底层数组
	s2[0] = 100
	fmt.Println("s1: ", s1)
	fmt.Println("s2: ", s2)

	// 切片的拷贝
	a := []int{1, 2, 3, 4, 5}
	b := make([]int, 5, 5)
	copy(b, a)
	fmt.Println("a: ", a)
	fmt.Println("b: ", b)
	b[0] = 10
	fmt.Println("a: ", a)
	fmt.Println("b: ", b)

}
// 切片的遍历
func sectionForRange()  {
	s := []int{1, 3, 5}
	for i :=0; i < len(s); i++{
		fmt.Printf("i:%v\n s[i]:%v\n", i, s[i])
	}

	// for...range
	for index, value := range s {
		fmt.Println(index, value)
	}
}


// 切片的增加
func sectionCrud()  {

	// append()
	var numSlice []int
	var otherSlice = []int{1, 2, 3}
	for i := 0; i < 10; i++ {
		numSlice = append(numSlice, i)
		fmt.Printf("%v --- %d --- %d --- ptr:%p\n", numSlice, len(numSlice), cap(numSlice), numSlice)
	}
	numSlice = append(numSlice, otherSlice...)
	fmt.Printf("%v\n", numSlice)


	// 切片的扩容
	// $GOROOT/src/runtime/slice.go
}

// 切片的删除
func sectionDelete()  {
	s := []int{1, 2, 3, 4, 5, 6, 7}
	// 删除元素4
	s = append(s[:3], s[4:]...)
	fmt.Printf("%v\n", s)
}


// ---------------- map -----------------
func mapUse()  {
	// map 的定义赋值
	scoreMap := make(map[string]int, 8)
	scoreMap["A"] = 100
	scoreMap["B"] = 90
	fmt.Println(scoreMap)
	fmt.Println(scoreMap["A"])
	fmt.Printf("type of a:%T\n", scoreMap)
	userInfo := map[string]string{
		"A": "A1",
		"B": "B",
	}
	fmt.Println("userInfo: ", userInfo)
}
// 判断某个键是否存在
func mapJudgeKey()  {
	userInfo := map[string]string{
		"A": "A1",
		"B": "B",
	}
	v, ok := userInfo["A"]
	if ok {
		fmt.Println(v)
	} else {
		fmt.Println("查无此人")
	}
}
// map的遍历
func forMap()  {
	tempMap := make(map[string]string)
	tempMap["A"] = "A1"
	tempMap["B"] = "B1"
	tempMap["C"] = "C1"
	// 获取键和值
	for k, v := range tempMap{
		fmt.Println(k, "---", v)
	}
	// 获取键
	for k := range tempMap{
		fmt.Println(k)
	}
	// 按指定顺序遍历map
	rand.Seed(time.Now().UnixNano()) //初始化随机数种子
	var TempMap = make(map[string]int, 200)
	for i := 0; i < 100; i++ {
		key := fmt.Sprintf("stu%02d", i) //生成stu开头的字符串
		value := rand.Intn(100)          //生成0~99的随机整数
		TempMap[key] = value
	}
	// 取出map中的所有key存入切片keys
	var keys = make([]string, 0,  200)
	for key := range TempMap{
		keys = append(keys, key)
	}
	// 对切片进行排序
	sort.Strings(keys)
	//按照排序后的key遍历map
	for _, key := range keys {
		fmt.Println(key, TempMap[key])
	}
}
// delete()函数，删除键值对
func deleteKeyValue()  {
	tempMap := make(map[string]int)
	tempMap["A"] = 10
	tempMap["B"] = 20
	tempMap["C"] = 30
	for k, v := range tempMap{
		fmt.Println(k, "1---1", v)
	}
	fmt.Println("\n")
	delete(tempMap, "B")
	for k, v := range tempMap{
		fmt.Println(k, "2---2", v)
	}
}
//元素为map类型的切片
func valueMapSection()  {
	var sectionMap = make(map[string]string, 3)
	for index, value := range sectionMap{
		fmt.Printf("index:%v\n value:%v\n\n\n", index, value)
	}
	fmt.Println("after init")
	// 对切片中的map元素进行初始化
	sectionMap = make(map[string]string, 10)
	sectionMap["name"] = "XT"
	sectionMap["password"] = "123456"
	sectionMap["address"] = "LZ"
	for index, value := range sectionMap {
		fmt.Printf("index:%d\n value:%v\n", index, value)
	}
}
// 值为切片类型的map
func valueSection()  {
	var sliceMap = make(map[string][]string, 3)
	fmt.Println(sliceMap)
	fmt.Println("after init")
	key := "中国"
	value, ok := sliceMap[key]
	if !ok {
		value = make([]string, 0, 2)
	}
	value = append(value, "北京", "上海")
	sliceMap[key] = value
	fmt.Println(sliceMap)
}


//func main()  {
//	//initArray1()
//	//initArray2()
//	//initArray3()
//
//	//indexArray()
//
//	//multiArray()
//
//	//copyArray()
//
//	//a := [3]int{1, 2, 3}
//	//fmt.Println(arraySum(a))
//
//	// ------------- 切片 -------------
//	//knowSection()
//	//SectionExpress()
//	//SectionMake()
//
//	//sectionCompare()
//	//sectionAssignmentCopy()
//
//	//sectionForRange()
//
//	//sectionCrud()
//
////	sectionDelete()
//
//	// --------------- map --------------
//	//mapUse()
//	//mapJudgeKey()
//	//forMap()
//	//deleteKeyValue()
//	valueMapSection()
//	fmt.Println("------")
//	valueSection()
//}