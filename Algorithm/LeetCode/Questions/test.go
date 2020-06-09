/*
 * @Author: Nettor
 * @Date: 2020-06-09 17:31:30
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-09 17:33:35
 * @Description: file content
 */ 
 package main
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
    intSlice := mkIntSlice()
    stringIntMap := mkStringIntMap()

    intSlice = append(intSlice, 100)
    stringIntMap["a"] = 1

    println(intSlice[0])
    println(stringIntMap["a"])
}