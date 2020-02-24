#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (37.66%)
# Likes:    2435
# Dislikes: 317
# Total Accepted:    353.4K
# Total Submissions: 930.6K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
#
# Input: 1->2
# Output: false
#
# Example 2:
#
#
# Input: 1->2->2->1
# Output: true
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        while head:
            nodeVal = stack.pop()
            if nodeVal != head.val:
                return False
            head = head.next
        return True

# @lc code=end
