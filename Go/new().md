<!--
 * @Author: Nettor
 * @Date: 2020-06-09 17:40:24
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-09 17:49:17
 * @Description: file content
-->

"new()" function return a pointer, the pointer is to a newly allocated zero value of that type.

```go
func new(Type) *Type
```

```go
package main

import "fmt"

func main() {
    var a *int
    a = new(int) //return a pointer to a
    *a = 10
    fmt.Println(*a)
}
//output:
//10
```
