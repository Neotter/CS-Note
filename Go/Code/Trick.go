/*
 * @Author: Nettor
 * @Date: 2020-06-09 17:31:30
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-13 21:12:47
 * @Description: file content
 */ 
 package main

 import(
    . "fmt" //可以给引用的包重命名，这里"."代表可以省略包名直接调用方法名
    "unicode/utf8" //用于解析utf8的字符
    "log"
    )
//initialize and return a int slice
func mkIntSlice() []int {
    s := make([]int,0,10)
    return s
}
//initialize and return a int/string map
func mkStringIntMap() map[string]int {
    m := make(map[string]int)
    return m
}

func main() {
    //测试怎么添加map和切片
    intSlice := mkIntSlice()
    stringIntMap := mkStringIntMap()

    intSlice = append(intSlice, 100)
    stringIntMap["a"] = 1

    println(intSlice[0])
    println(stringIntMap["a"])
    //测试切片是否可以用x[n]的方式调用
    x := make([]int,10)
    x[0] = 2
    Println(x)
    //测试String的修改
    text := "text"
    xbytes := []byte(text)//转换成byte slice
    xbytes[0] = 'T'
    Println("text变成了 ",text)
    //"%T"打印目标类型，String[n]返回的是byte类型的值
    //只用使用Printf才会格式化字符串，Println等等都不行
    Printf("text的类型是:%T\n",text[0])
    //用len并不能准确计算字符串类型，因为go使用的是utf8
    //所以需要通过utf8包下的RuneCountInString()方法进行计算
    data := "♥"
    Println("len()方法输出 ",len(data))
    Println("RuneCountInString()方法输出 ", utf8.RuneCountInString(data))
    //多行数组最后一行一定需要逗号，我是觉得如果需要增加内容的话挺方便的
    multiRowArray := []int{
        1,
        2,//最后一行
    }
    singleRowArray := []int{3,4,}//单行的话多一个都逗号也正确
    multiRowArray = multiRowArray//变量一定要使用才能通过编译，就让他自己等于自己
    singleRowArray = singleRowArray
    //log.Fatal和log.Panic会直接推出程序,log.Println不会
    //log.Fatalln("Fatal Level: log entry") //app exits here
    log.Println("Normal Level: log entry") //app do not exits here
    //不能使用精简赋值语句对变量重新赋值，
    //但是可以通过精简赋值的多变量赋值功能变量重新赋值
    //比如刚刚变量x已经用过了
    //x := "aaa" ///出错
    text,y := "aaaa","bc"
    text = text
    y = y //x,y虽然都是string,但由于x和y的字数不同所以不能把y赋值给x
    //nil只能赋值给interface，function，pointer，map，slice和channel
    //var x = nil //error
    var intfX interface{} = nil
    intfX = intfX
    //for range 的range一定会返回两个值，不能省略
    xArray := []string{"a","b","c"}
    for _,v:=range xArray{
        Println(v)
    }
}