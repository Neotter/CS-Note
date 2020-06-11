<!--
 * @Author: Nettor
 * @Date: 2020-06-11 12:34:57
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-11 15:34:53
 * @Description: file content
-->

# 3 ways to implement stack with Golang

## Using Slice

```go
package main

import(
    "fmt"
    "sync"
)

// Item: the type of the stack
type Item interface{}

// ItemStack: the stack of Items
type ItemStack struct {
    items []Item
    lock sync.RWMutex
}

// New creates a new ItemStack
func NewStack() *ItemStack {
    s := &ItemStack {}
    s.items = []Item{}
    return s
}

// Print: prints all the elements
func (s *ItemStack) Print() {
    fmt.Println(s.items)
}

// Push: add an Item on the top of the stack
func (s *ItemStack) Push(t Item) {
    s.lock.Lock()
    defer s.lock.Unlock()
    s.items = append(s.items, t)
}

// Pop: remove an Item from the top of stack
func (s *ItemStack) Pop() interface{} {
    s.lock.Lock()
    defer s.lock.Unlock()
    if len(s.items) == 0{
        return nil
    }
    item := s.items[len(s.items)-1]
    s.items = s.items[0:len(s.items)-1]
    return item
}

// IsEmpty: Determine if the stack is empty
func (s *ItemStack) IsEmpty() bool {
    if len(s.items) == 0 {
        return true
    } else {
        return false
    }
}
```

### Performance

```go
package main

import (
    "testing"
)

var stack *ItemStack

func init() {
    stack = NewStack()
}

func Benchmark_Push(b *testing.B) {
    for i := 0; i < b.N; i++ { //use b.N for looping
        stack.Push("test")
    }
}

func Benchmark_Pop(b *testing.B) {
    b.StopTimer()
    for i := 0; i < b.N; i++ { //use b.N for looping
        stack.Push("test")
    }
    b.StartTimer()
    for i := 0; i < b.N; i++ { //use b.N for looping
        stack.Pop()
    }
}
```

```shell
$ go test -test.bench=".*" -benchmem -v
goos: darwin
goarch: amd64
pkg: test/test8
Benchmark_Push-4       10000000             222 ns/op          94 B/op           0 allocs/op
Benchmark_Pop-4        20000000            65.0 ns/op           0 B/op           0 allocs/op
PASS
ok      test/test8    7.644s
```

## Using container/list

```go
package main

import(
    "container/list"
    "sync"
)

type Stack struct {
    list *list.List
    lock *sync.RWMutex
}

func NewStack() *Stack {
    list := list.New()
    l := &sync.RWMutex{}
    return &Stack{list,l}
}

func (stack *Stack) Push(value interface{}) {
    stack.lock.Lock()
    defer stack.lock.Unlock()
    e := stack.list.Back()
    if e!= nil {
        stack.list.Remove(e)
        return e.Value
    }
    return nil
}

func (stack *Stack) Peak() interface{} {
    e := stack.list.Back()
    if e != nil {
        return e.Value
    }

    return nil
}

func (stack *Stack) Len() int {
    return stack.list.Len()
}

func (stack *Stack) IsEmpty() bool {
    return stack.list.Len() == 0
}
```

### Performance

```shell
$ go test -test.bench=".*" -benchmem -v  -count=1
goos: darwin
goarch: amd64
pkg: test/test10
Benchmark_Push-4        5000000           222 ns/op          48 B/op           1 allocs/op
Benchmark_Pop-4        20000000            73.5 ns/op           0 B/op           0 allocs/op
PASS
ok      test/test10    10.837s
```

## godoc Reference

```go
package main

import (
    "sync"
)

type (
    Stack struct {
        top    *node
        length int
        lock   *sync.RWMutex
    }
    node struct {
        value interface{}
        prev  *node
    }
)

// Create a new stack
func NewStack() *Stack {
    return &Stack{nil, 0, &sync.RWMutex{}}
}

// Return the number of items in the stack
func (this *Stack) Len() int {
    return this.length
}

// View the top item on the stack
func (this *Stack) Peek() interface{} {
    if this.length == 0 {
        return nil
    }
    return this.top.value
}

// Pop the top item of the stack and return it
func (this *Stack) Pop() interface{} {
    this.lock.Lock()
    defer this.lock.Unlock()
    if this.length == 0 {
        return nil
    }
    n := this.top
    this.top = n.prev
    this.length--
    return n.value
}

// Push a value onto the top of the stack
func (this *Stack) Push(value interface{}) {
    this.lock.Lock()
    defer this.lock.Unlock()
    n := &node{value, this.top}
    this.top = n
    this.length++
}
```

### Performance

```shell
$ go test -test.bench=".*" -benchmem -v
goos: darwin
goarch: amd64
pkg: test/test9
Benchmark_Push-4   	10000000	         178 ns/op	      32 B/op	       1 allocs/op
Benchmark_Pop-4    	20000000	        75.5 ns/op	       0 B/op	       0 allocs/op
PASS
ok  	test/test9	9.776s
```
