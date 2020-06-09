/*
 * @Author: Nettor
 * @Date: 2020-06-08 20:03:43
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-08 20:10:37
 * @Description: file cont
 */ 
package main
 import(
	"fmt"
)

func main(){
	fmt.Println("Hello")
	x := [...]int{0,1,2}
	y := x[0]
	y = 2
	fmt.Println(x,y)
}