<!--
 * @Author: Nettor
 * @Date: 2020-06-20 21:23:58
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-20 22:05:13
 * @Description: file content
-->

# Sort String

## Solution 1

```go
func SortString(w string) string {
    s := strings.Split(w, "")
    sort.Strings(s)
    return strings.Join(s, "")
}
```

## Solution 2

Rune version

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

func sortString(s string) string {
    r := []rune(s)
    sort.Sort(sortRunes(r))
    return string(r)
}
```

Byte version(fast than Rune version and Solution 1)

```go
type sortBytes []byte

func (s sortBytes) Less(i, j int) bool {
    return s[i] < s[j]
}

func (s sortBytes) Swap(i, j int) {
    s[i], s[j] = s[j], s[i]
}

func (s sortBytes) Len() int {
    return len(s)
}

func SortString(s string) string {
    r := []byte(s)
    sort.Sort(sortBytes(r))
    return string(r)
}
```
