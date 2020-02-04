#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (29.38%)
# Likes:    7435
# Dislikes: 438
# Total Accepted:    1.3M
# Total Submissions: 4.3M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
#
# Example 2:
#
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
#
# Example 3:
#
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
#
#
#
#
#
#

# @lc code=start


class Solution:
    # Hash
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        charDict = {}

        for i in range(len(s)):
            if s[i] in charDict and start <= charDict[s[i]]:
                start = charDict[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            charDict[s[i]] = i

        return maxLength
# @lc code=end
