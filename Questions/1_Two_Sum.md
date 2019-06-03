# LeetCode No.1: Two Sum

### Question:

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

### Example:

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

### Solution:

### Code_Python:

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        for num in nums_sorted:
            b = target - num
            if nums.count(b) == 1:
                b_index = nums.index(b)
                a_index = nums.index(num)
                return [a_index, b_index]
            if nums.count(b) > 1:
                a_index = nums.index(b)
                nums[a_index] = -1
                b_index = nums.index(b)
                return [a_index, b_index]
        return
```

### Code_java: