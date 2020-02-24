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
        fast = slow = head
        rev = None
        # 双指针,快的走的速度是慢的两倍,当快的到达终点之后,慢的指针正好在中间
        # 慢的指针每走一步都翻转链表,当快的指针到达终点时,前半部分的链表就翻转了
        # python3中的连续赋值并不是按顺序赋值
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev

# @lc code=end
