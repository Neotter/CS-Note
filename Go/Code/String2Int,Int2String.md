<!--
 * @Author: Nettor
 * @Date: 2020-06-20 21:18:58
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-20 21:19:36
 * @Description: file content
-->

# String to Int, Int to String

string 转成 int：
int, err := strconv.Atoi(string)

string 转成 int64：
int64, err := strconv.ParseInt(string, 10, 64)

int 转成 string：
string := strconv.Itoa(int)

int64 转成 string：
string := strconv.FormatInt(int64,10)
