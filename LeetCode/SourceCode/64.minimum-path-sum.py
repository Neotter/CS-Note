#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (50.19%)
# Likes:    1984
# Dislikes: 47
# Total Accepted:    296.6K
# Total Submissions: 589.7K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
#
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
#
#
#

# @lc code=start


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # row number and column nuber
        n = len(grid)
        m = len(grid[0])
        # stop condition
        if n <= 0 or m <= 0:
            return 0
        # init dp map
        # dp = [[0] * m] * n
        dp = [[0 for j in range(m)] for i in range(n)]
        dp[0][0] = grid[0][0]
        # init dp row of dp map
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        # init dp column of dp map
        for i in range(1, m):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        # dp calculate the final result
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]

# @lc code=end
