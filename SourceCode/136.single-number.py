#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (62.45%)
# Likes:    3421
# Dislikes: 135
# Total Accepted:    620.4K
# Total Submissions: 987.9K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,1]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,1,2,1,2]
# Output: 4
#
#
#

# @lc code=start


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

# @lc code=end
