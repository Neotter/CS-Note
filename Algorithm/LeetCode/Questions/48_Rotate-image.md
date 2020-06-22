<!--
 * @Author: Nettor
 * @Date: 2020-06-22 15:49:49
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-22 15:51:36
 * @Description: file content
-->

# Rotate image

## Go Solution

```go
func rotate(matrix [][]int)  {
    //reverse matrix
    end := len(matrix)-1
    mid := int(math.Floor(float64(end/2)))
    for i:=0;i<=mid;i++{
        matrix[i],matrix[end-i] = matrix[end-i],matrix[i]
    }
    for i:=0;i<=end;i++{
        for j:=0;j<=i;j++{
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        }
    }
}
```

- 方便的交换方法: `matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]`
