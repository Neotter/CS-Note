#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (28.08%)
# Likes:    5760
# Dislikes: 865
# Total Accepted:    578.8K
# Total Submissions: 2.1M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
#
# Example 2:
#
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#
#
#

# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        maxValue = float("inf")
        minValue = float("-inf")
        # get length of nums 1&2
        lenN1 = len(nums1)
        lenN2 = len(nums2)
        # choise the shortest array as the binary search array
        if lenN1 > lenN2:
            return self.findMedianSortedArrays(nums2, nums1)
        # if nums1 is empty, nums2 contain the median, return it directly
        if lenN1 == 0:
            if lenN2 % 2 == 0:
                return ((nums2[int(lenN2 / 2) - 1] + nums2[int((lenN2) / 2)]) / 2)
            else:
                return nums2[int(lenN2/2)]
        lenAll = lenN1 + lenN2
        # cutting range
        cutL = 0
        cutR = lenN1
        # cutting position
        cutN1 = int(lenN1 / 2)
        cutN2 = lenAll / 2 - cutN1

        while cutN1 <= lenN1:
            cutN1 = int((cutR - cutL) / 2 + cutL)
            cutN2 = int(lenAll / 2 - cutN1)

            L1 = minValue if cutN1 == 0 else nums1[cutN1 - 1]
            R1 = maxValue if cutN1 == lenN1 else nums1[cutN1]
            L2 = minValue if cutN2 == 0 else nums2[cutN2 - 1]
            R2 = maxValue if cutN2 == lenN2 else nums2[cutN2]
            if L1 > R2:
                cutR = cutN1 - 1
            elif L2 > R1:
                cutL = cutN1 + 1
            else:
                if lenAll % 2 == 0:
                    L1 = max(L1, L2)
                    R1 = min(R1, R2)
                    return (L1 + R1) / 2
                else:
                    R1 = min(R1, R2)
                    return R1
        return -1
# @lc code=end
