/*
 * @Author: Nettor
 * @Date: 2020-06-08 20:03:43
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-11 15:23:10
 * @Description: file cont
 */ 
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

//Test
func main() {
    stack := NewStack()
    for i:=1;i<=10;i++{
        stack.Push(i)
    }
    stack.Print()
    fmt.Println(stack.IsEmpty())
    for i:=1;i<=10;i++{
        fmt.Println(stack.Pop())
    } 
    fmt.Println(stack.IsEmpty())
}