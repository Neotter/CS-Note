#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.50%)
# Likes:    6742
# Dislikes: 1746
# Total Accepted:    1.2M
# Total Submissions: 3.6M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 定义进位,如果有进位carry等于一,如果没有进位等于0
        carry = 0
        # 定义根节点
        root = current = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                current.val += l1.val
                l1 = l1.next
            if l2:
                current.val += l2.val
                l2 = l2.next
            # divmod的功能是互相取余数,输入a,b,输出a对b的余数,b对a的余数
            carry, current.val = divmod(current.val + carry, 10)
            # 如果下一个还有值
            if l1 or l2 or carry:
                current.next = ListNode(0)
                current = current.next
        return root

# @lc code=end
