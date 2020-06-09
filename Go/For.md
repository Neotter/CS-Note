<!--
 * @Author: Nettor
 * @Date: 2020-06-08 20:17:26
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-08 21:23:22
 * @Description: file content
-->

# For

① for init; condition; post { }

```go
    for i := 0; i < 3; i++ {  }
```

"init" will only be executed once.

② for condition { }

```go
    for x < 10 { }
```

"condition" will be executed repeatedly.

③ for { }

```go
    for { break }
```

④ for...range {}

It support string,array,\*array,slice,map,channel,key and value.

```go
func main() {
    data := [3]string{"a","b","c"}
    for i,s := range data {
        println(i,s)
    }
}
//output:
//0 a
//1 b
//2 c
```

You can use "\_" replace key, it will only return value.

```go
func main() {
    data := [3]string{"a","b","c"}
    for _,s := data {
        println(s) // output: a b c
    }
}
//output:
//a
//b
//c
```

Or remove value, it will return key.

```go
func main() {
    data := [3]string{"a","b","c"}
    for i := data {
        println(i)
    }
}
//output:
//0
//1
//2
```

Key and value is local variable, they will be reused (address does not change).
