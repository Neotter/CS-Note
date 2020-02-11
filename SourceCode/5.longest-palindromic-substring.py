#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (28.54%)
# Likes:    5150
# Dislikes: 449
# Total Accepted:    761.2K
# Total Submissions: 2.7M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#
#

# @lc code=start


class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenS = len(s)
        # only one element, return directly
        if lenS <= 1:
            return s
        # init dp
        dp = [[None for i in range(lenS)] for j in range(lenS)]
        res = ""
        for i in range(lenS - 1, -1, -1):
            for j in range(i, lenS):
                dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i + 1][j - 1])
                if dp[i][j] and (res == "" or j - i + 1 > len(res)):
                    res = s[i:j + 1]
        return res

# @lc code=end
