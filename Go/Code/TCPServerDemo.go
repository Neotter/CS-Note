/*
 * @Author: Nettor
 * @Date: 2020-06-15 15:17:57
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-15 17:21:27
 * @Description: file content
 */
package main

import (
	"fmt"
	"io/ioutil"
	"net"
	"os"
	"time"
)

func main() {
	//获取ip地址
	tcpAddr, err := net.ResolveTCPAddr("tcp", ":8080")
	checkError(err)
	//开始监听端口
	listener, err := net.ListenTCP("tcp", tcpAddr)
	checkError(err)
	for {
		conn, err := listener.Accept()
		//错误的话继续监听
		if err != nil {
			fmt.Println(err)
			continue
		}
		//返回对应的时间
		go handleClient(conn)
	}

}

func handleClient(conn net.Conn) {
	defer conn.Close()
	//读取客户端传过来的信息,一定要用协程处理，不然会出错
	go func() {
		response, _ := ioutil.ReadAll(conn)
		fmt.Println(string(response))
	}()
	daytime := time.Now().String()
	conn.Write([]byte(daytime))
}

func checkError(err error) {
	if err != nil {
		fmt.Println("Fatal error :", err.Error())
		os.Exit(1)
	}
}
