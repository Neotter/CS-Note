/*
 * @Author: Nettor
 * @Date: 2020-06-08 20:03:43
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-09 13:06:33
 * @Description: file cont
 */ 
package main

type Stack []interface {}

func (stack Stack) Len() int {
    return len(stack)
} 

func (stack Stack) Cap() int {
    return cap(stack)
}

func (stack *Stack) Push(value interface{}) {
    *stack = append(*stack, value)
}

func (stack *Stack) Pop() (interface{}, error) {
    theStack := *stack
    if len(theStack) == 0 {
        return nil, errors.New("Out of index, len is 0.")
    }
    value := theStack[len(theStack) - 1]
    *stack = theStack[:len(theStack) - 1]
    return value,nil
}

func (stack Stack) Top() (interface{}, error){
    if len(stack) == 0{
        return nil,errors.New("Out of index, len is 0")
    }
    return stack[len(stack) -1], nil
}

func (stack Stack) isEmpty() bool{
    return len(stack) == 0
}