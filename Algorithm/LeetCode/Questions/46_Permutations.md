<!--
 * @Author: Nettor
 * @Date: 2020-06-11 12:16:53
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-11 12:19:56
 * @Description: file content
-->

# Permutations

## Java Solution

```java
class Solution {
List<List<Integer>> ret = new ArrayList<>();

public List<List<Integer>> permute(int[] nums) {
 if(nums.length == 0)
return ret;

        backtracking(nums, new boolean[nums.length],new ArrayList<>());
        return ret;
    }

    private void backtracking(int[] nums, boolean[] numsHasUsed,List<Integer> path){
        if(path.size() == nums.length){
            ret.add(new ArrayList<>(path));//需要注意的是这一行，一定要把path转换为ArrayList才正常，我也不知道为啥
        }
        for(int i=0; i < nums.length; i++){
            if(!numsHasUsed[i]){
                numsHasUsed[i] = true;
                path.add(nums[i]);
                backtracking(nums, numsHasUsed,path);
                path.remove(path.size() - 1);
                numsHasUsed[i] = false;
            }
        }
    }
}
```

```go

```
