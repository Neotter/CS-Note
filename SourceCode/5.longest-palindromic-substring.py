#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start


class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenS = len(s)
        if lenS <= 1:
            return s
        dp = [[None for i in range(lenS)] for j in range(lenS)]
        resLeft = resRight = 0
        # init dp
        for i in range(lenS):
            dp[i][i] = True
            dp[i][i-1] = True
        for lenP in range(2, lenS):
            for i in range(lenS - lenP):
                if s[i] == s[i + lenP - 1] and dp[i + 1][i + lenP - 2]:
                    dp[i][i + lenP - 1] = True
                    if resLeft - resLeft + 1 < lenP:
                        resLeft = i
                        resRight = i + lenP - 1
        return s[resLeft:resRight-resLeft+1]
# @lc code=end
