#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (55.39%)
# Likes:    2432
# Dislikes: 201
# Total Accepted:    502.6K
# Total Submissions: 901.4K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always
# exist in the array.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
#
#

# @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        return int(max(map, key=map.get))
# @lc code=end
