#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#
# https://leetcode.com/problems/hamming-distance/description/
#
# algorithms
# Easy (70.95%)
# Likes:    1513
# Dislikes: 148
# Total Accepted:    280.2K
# Total Submissions: 394.4K
# Testcase Example:  '1\n4'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 2^31.
#
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
#
# The above arrows point to positions where the corresponding bits are
# different.
#
#
#

# @lc code=start


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        for i in bin(x ^ y)[2:]:
            if i == '1':
                res += 1
        return res
# @lc code=end