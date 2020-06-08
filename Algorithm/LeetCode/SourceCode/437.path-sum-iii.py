#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (44.51%)
# Likes:    2681
# Dislikes: 198
# Total Accepted:    149.2K
# Total Submissions: 333.4K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go
# downwards
# (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range
# -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # Edge state
        if not root:
            return 0

        # Processing
        def dfs(node, sum):
            count = 0
            if not node:
                return 0
            if node.val == sum:
                count += 1
            count += dfs(node.left, sum - node.val)
            count += dfs(node.right, sum - node.val)
            return count

        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
# @lc code=end
