#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (52.50%)
# Likes:    3075
# Dislikes: 97
# Total Accepted:    471.1K
# Total Submissions: 881.5K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of
# times.
#
# Note:
#
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#
#
#

# @lc code=start


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)
# @lc code=end
