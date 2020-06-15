/*
 * @Author: Nettor
 * @Date: 2020-06-15 13:59:52
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-15 17:16:58
 * @Description: file content
 */
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Fprintf(os.Stderr, "Usage: %s host:port", os.Args[0])
		//log.Printf(err.Error(),, "Usage: %s host:port", os.Args[0])
		os.Exit(1)
	}
	//首先我们根据用户的输入通过net.ResolveTCPAddr获取了一个tcpaddr,然后DialTCP获取了一个TCP链接，然后发送请求信息，最后通过ioutil.ReadAll读取全部的服务器反馈信息
	service := os.Args[1]
	//通过ResolveTCPArrd获取一个TCPAddr,net表示tcp4 tcp6 tcp任意一个，addr表示域名或者IP地址
	//func ResolveTCPAddr(net, addr string) (*TCPAddr, error)
	tcpAddr, err := net.ResolveTCPAddr("tcp4", service)
	checkError(err)
	//建立一个TCP链接，返回TCPConn类型
	//func DialTCP(net string, laddr, raddr *TCPAddr) (c *TCPConn, err os.Error)
	conn, err := net.DialTCP("tcp4", nil, tcpAddr)
	checkError(err)
	//TCPConn中的Read和Write可以用于client和server之间的数据传输
	_, err = conn.Write([]byte("HEAD / HTTP/1.0\r\n\r\n"))
	checkError(err)
	//读取返回的结果
	result, err := ioutil.ReadAll(conn)
	checkError(err)
	fmt.Println(string(result))
	os.Exit(0)
}

func checkError(err error) {
	if err != nil {
		log.Printf("%T %+v", err, err)
		os.Exit(1)
	}
}
