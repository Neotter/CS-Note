#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (45.37%)
# Likes:    6250
# Dislikes: 267
# Total Accepted:    769K
# Total Submissions: 1.7M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
#
#

# @lc code=start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        maximum = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            maximum = max(maximum, dp[i])
        return maximum

# @lc code=end
