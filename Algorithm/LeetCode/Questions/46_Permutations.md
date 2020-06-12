<!--
 * @Author: Nettor
 * @Date: 2020-06-11 12:16:53
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-12 13:27:37
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
            return;
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

## Go Solution

```go
func permute(nums []int) [][]int {
    var ret = make([][]int,0)
    if len(nums) == 0{
        return ret
    }
    numsHasUsed := make([]bool,len(nums))
    path := make([]int,0,len(nums))
    backtracking(nums,&numsHasUsed,&path,&ret)
    return ret
}

func backtracking(nums []int, numsHasUsed *[]bool, path *[]int, ret *[][]int) {
    if len(*path) == len(nums) {
        //因为path是切片，里面的数组的地址是指针，如果直接append到ret里面后续path有修改的话也会直接影响到已经保存到ret里面的值，因此每次保存到ret里面都要手动复制一份
        t := make([]int,len(nums))
        copy(t,*path)
        *ret = append(*ret, t)
        return
    }
    for i:=0; i<len(nums); i++ {
        if !(*numsHasUsed)[i] {
            (*numsHasUsed)[i] = true
            *path = append(*path,nums[i])
            backtracking(nums,numsHasUsed,path,ret)
            *path = (*path)[:len(*path)-1]
            (*numsHasUsed)[i] = false

        }
    }
}
```
