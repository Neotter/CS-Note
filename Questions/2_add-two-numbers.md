# LeetCode No.1: Two Sum

## Question:

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

## Example:

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

## Solution:

(为了节约空间,也可以不新建一个链表直接用旧的链表用于保存.)

step.1 初始化一个新链表和一个表示进位的变量.
step.2 同时遍历两个链表,每遍历一步就把两个节点相加,之后让指针指向下一个节点.
step.3 相加之后的数对 10 取余,把进位提出存在另一个变量上, 并把余数存在新的链表里面.
step.4 判断两个链表的下一个节点和进位是不是都存在,如果都存在那么新建下一个节点,保存它们
