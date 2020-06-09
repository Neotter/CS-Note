<!--
 * @Author: Nettor
 * @Date: 2020-06-09 16:35:35
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-09 17:48:45
 * @Description: file content
-->

# Reference type

Slice, map and channel are called reference types.

Reference types must be initialized by "make()" function.

```go
    func make(Type) Type {} //map,slice,channel
    func make(Type, len IntegerType) Type {} //slice
    func make(Type, len IntegerType, cap IntegerType) Type {} //slice
```

```go
//initialize and return a int slice
func mkIntSlice() []int {
    s := make([]int,0,10)
    return s
}
//initialize and return a int/string map
func mkStringIntMap() map[string]int {
    s := make(map[string]int)
    return m
}

func main() {
    intSlice := mkIntSlice()
    stringIntMap := mkIntStringMap()

    intSlice = append(intSlice, 100)
    stringIntMap["a"] = 1

    println(intSlice[0])
    println(stringIntMap["a"])
}
//output:
//100
//1
```

"new()" function also can allocate memory to a reference type.
However, it doesn't fully create a reference type.

For example, while using "new()" to create a map, it doesn't allocate memory of key/value, so it will cause panic.

```go
func main() {
    p := new(nap[string]int)
    m := *p
    m["a"] = 1 //panic: assignment to entry in nil map
    println(m["a"])
}
```
