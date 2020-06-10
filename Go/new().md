<!--
 * @Author: Nettor
 * @Date: 2020-06-09 17:40:24
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-09 18:24:44
 * @Description: file content
-->

# new()

"new()" function return a pointer, the pointer is to a newly allocated zero value of that type.

Usually we use "new()" to initailize a basic type link int, bool, byte...

"new()" can't be used for reference type like slice, map, chan.

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
