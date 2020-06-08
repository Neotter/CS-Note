# LeetCode No.1: Two Sum

## Question:

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Example:

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

## Solution:

新建一个字典,key 为 target - num, value 为 num 的 index, 每当循环到一个新的数时,对比字典中是否存在相等的 key, 如果不存在继续循环下一个数, 如果存在, 输出相应的 key 的 value 和当前循环到的 num 的 index.
