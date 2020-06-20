<!--
 * @Author: Nettor
 * @Date: 2020-06-18 15:12:01
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-20 21:45:01
 * @Description: file content
-->

# String

String is a immutable byte

```go
type stringStruct struct {
    str unsage.Pointer
    len int
}
```

## Sort Element in String

```go
type sortRunes []rune

func (s sortRunes) Less(i, j int) bool {
    return s[i] < s[j]
}

func (s sortRunes) Swap(i, j int) {
    s[i], s[j] = s[j], s[i]
}

func (s sortRunes) Len() int {
    return len(s)
}

func SortString(s string) string {
    r := []rune(s)
    sort.Sort(sortRunes(r))
    return string(r)
}
```
