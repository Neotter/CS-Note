#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Easy (30.64%)
# Likes:    2098
# Dislikes: 106
# Total Accepted:    99.6K
# Total Submissions: 324.5K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# Given an integer array, you need to find one continuous subarray that if you
# only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
#
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
#
#
#
# Note:
#
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means .
#
#
#

# @lc code=start


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 排完序之后就好办了
        sortedNums = sorted(nums)
        start, end = -1, -1
        for i in range(len(nums)):
            if nums[i] != sortedNums[i]:
                start = i
                break
        if start == -1:
            return 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != sortedNums[i]:
                end = i
                break
        return end - start + 1

# @lc code=end
