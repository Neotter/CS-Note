# LeetCode No.4: Median of Two Sorted Arrays

## Question

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

### Example 1

```Python
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

### Example 2

```Python
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

## Solution

For example, there are two array like this:

| Index | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nums1 | 3   | 5   | 8   | 9   |     |     |
| nums2 | 1   | 2   | 7   | 10  | 11  | 12  |
| nums3 | 1   | 2   | 3   | 5   | 7   | 8   | 9   | 10  | 11  | 12  |

As we can see, nums3 is the combination of nums1 and nums2.

The median of nums3 is (7 + 8)/2.

Their index is 4 and 5.

Even if the length of nums3 is odd, the median split the nums3 into two parts(denote as Lpart and Rpart) with equal length.

We can get this length as follow.

```python
lenN3 = int((len(nums1) + len(nums2))) / 2
# int() function discard the remainder

# If nums3 is odd(e.g. nums3=[1,2,3]), the median split nums3 into Lpart = [1] and Rpart = [3]. The length of each part is int(len(nums3)/2) =

# If nums3 is even(e.g. nums3=[1,2,3,4]), the median split nums3 into Lpart = [1,2] and Rpart = [3,4]. The length of each part is int int(len(nums3)/2) = 2
```

Because the elements in each part is from the nums1 and nums2 and nums1 and nums2 are ordered.

In nums1 and nums2 , if we found which element consist into Lpart, the Rpart will also known.

Moreover, in nums1, if we known which elements consist into Lpart, because the length of Lpart is fix, the rest of elements in Lpart is first N elements in nums2.

N can be calculated by subtracting length of element in nums1 which consist into Lpart from length of Lpart

For example

|       | Lpart       | Rpart          |
| ----- | ----------- | -------------- |
| nums3 | [1,2,3,5,7] | [8,9,10,11,12] |
| nums1 | [3,5]       | [8,9]          |
| nums2 | [1,2,7]     | [10,11,12]     |

From the table, length of Lpart of nums3 is 5.

[3,5] are from nums1, length is 2.

By substracting 2 from 5, we can know the element from 0 to 2 in nums2, is the rest of element in Lpart of nums3.

In the meanwhile, the max value in Lpart of nums1(which is 5, the lastest element in Lpart) is lower than the min value in Rpart of nums2(which is 10, first element in Rpart).

The max value in Lpart of nums2(which is 7, the lastest element in Lpart) is lower than the min value in Rpart of nums1(which 8, first element in Rpart).

In brief

```python
nums1.Lpart[-1] <= nums2.Rpart[0],
nums2.Lpart[-1] <= nums1.Rpart[0]
```

So, we just need to find out the correct postiton of the cutting which meet the above condition in nums1 than can get the median.

For saving times, we use binary search to find the correct postion.

There are 3 result after we cut:

First.

```python
nums1.Lpart[-1] > nums2.Rpart[0]
```

|       | Lpart   | Rpart        |
| ----- | ------- | ------------ |
| nums1 | [3,5,8] | [9]          |
| nums2 | [1,2]   | [7,10,11,12] |

We need to move the cutting positon left.

Second.

```python
nums2.Lpart[-1] > nums1.Rpart[0]
```

|       | Lpart      | Rpart   |
| ----- | ---------- | ------- |
| nums1 | [3]        | [5,8,9] |
| nums2 | [1,2,7,10] | [11,12] |

We need to move the cutting postion right.

Third.

```python
nums1.Lpart[-1] <= nums2.Rpart[0],
nums2.Lpart[-1] <= nums1.Rpart[0]
```

|       | Lpart   | Rpart      |
| ----- | ------- | ---------- |
| nums1 | [3,5]   | [8,9]      |
| nums2 | [1,2,7] | [10,11,12] |

Output the result.

### DLC.

To prevent boundary problem, we can add a global minimum and global maximum.

For saving time, we can use the shortest array as binary search array.

If the shortest array is empty, output the median of the other array directly.
