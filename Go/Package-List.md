<!--
 * @Author: Nettor
 * @Date: 2020-06-11 17:10:12
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-11 21:48:16
 * @Description: file content
-->

# Package-List

Import List package.

```go
import(
    "container/list"
)
```

# type List

## func New()

New and initialize a list instance.

```go
//func New() *List
listA := list.New() //Type of listA is *list.List
```

## func (\*List) PushBack & func (\*List) PushFront

- Inserts a new element at the back of list and returns element itself.
- Inserts a new element at the front of list and returns element itself.

```go
//func (l *List) PushBack(v interface{}) *Element
//func (l *List) PushFront(v interface{}) *Element
element := 1
elementPointer := listA.pushBack(element)
// *elementPointer == 1
// listA{1}
element := 0
elementPointer = listA.pushBack(element)
// *elementPointer == 0
// listA{0,1}

```

## func (\*List) PushBackList & func (\*List) PushFrontList

- PushBackList inserts a copy of an other list at the back of list l. The lists l and other may be the same. They must not be nil.
- PushFrontList inserts a copy of an other list at the front of list l. The lists l and other may be the same. They must not be nil.

```go
//func (l *List) PushBackList(other *List)
//func (l *List) PushFrontList(other *List)
listB := list.New()
element := 2
listB.Push(element)
//listB{2}
listA.PushBackList(listB)
//listA{0,1,2}
listC := list.New()
element := -1
listC.Push(element)
//listC{-1}
listA.PushBackList(listC)
//listA{-1,0,1,2}
```

## func (\*List) Back & func (\*List) Front

- Returns the last element of list, if list empty, return nil.
- Returns the first element of list, if list empty, return nil.

```go
//func (l *List) Back() *Element
//func (l *List) Front() *Element

if elementPointer :=  listA.Back(), element1 == nil {
    println("listA is empty!")
}
//*elementPointer == 2
//listA{-1,0,1,2}
if elementPointer :=  listA.Front(), element1 == nil {
    println("listA is empty!")
}
//*elementPointer == -1
//listA{-1,0,1,2}
```

## func (\*List) InsertAfter & func (\*List) InsertBefore

- InsertAfter inserts a new element e with value v immediately after mark and returns e. If mark is not an element of l, the list is not modified. The mark must not be nil.
- InsertBefore inserts a new element e with value v immediately before mark and returns e. If mark is not an element of l, the list is not modified. The mark must not be nil.

```go
//func (l *List) InsertAfter(v interface{}, mark *Element) *Element
//func (l *List) InsertBefore(v interface{}, mark *Element) *Element
element := 3
lastElementAtListA := listA.Back()
lastElementAtListA = listA.InsertAfter(element,lastElementAtListA)
//listA{-1,0,1,2,3}
//*lastElementAtListA == 3
//lastElementAtListA == listA.Back()
element := -2
FirstElementAtListA := listA.Front()
FirstElementAtListA = listA.InsertBefore(element,FirstElementAtListA)
//listA{-2,-1,0,1,2,3}
//*FirstElementAtListA == -2
//FirstElementAtListA == listA.Front()
```

## func (\*List) Len

- Len returns the number of elements of list l. The complexity is O(1).

```go
//func (l *List) Len() int
println(listA.len())
//output:
//6
```

## func (\*List) MoveAfter & func (\*List) MoveBefore

- MoveAfter moves element e to its new position after mark. If e or mark is not an element of l, or e == mark, the list is not modified. The element and mark must not be nil.
- MoveBefore moves element e to its new position before mark. If e or mark is not an element of l, or e == mark, the list is not modified. The element and mark must not be nil.

```go
//func (l *List) MoveAfter(e, mark *Element)
//func (l *List) MoveBefore(e, mark *Element)
firstElement := listA.Front()
lastElemetn := listA.Back()
listA.MoveAfter(firstElement,lastElement)
//listA{-1,0,1,2,3,-2}
firstElement := listA.Front()
lastElemetn := listA.Back()
listA.MoveBefore(lastElement,firstElement)
//listA{-2,-1,0,1,2,3}
```

## func (\*List) MoveToBack & func (\*List) MoveToFront

- MoveToBack moves element e to the back of list l. If e is not an element of l, the list is not modified. The element must not be nil.
- MoveToFront moves element e to the front of list l. If e is not an element of l, the list is not modified. The element must not be nil.

```go
//func (l *List) MoveToBack(e *Element)
//func (l *List) MoveToFront(e *Element)
firstElement := listA.Front()
listA.MoveToBack(firstElement)
//listA{-1,0,1,2,3,-2}
lastElemetn := listA.Back()
listA.MoveToFront(lastElemetn)
//listA{-2,-1,0,1,2,3}
```

## func (\*List) Remove

- Remove removes e from l if e is an element of list l. It returns the element value e.Value. The element must not be nil.

```go
//func (*List) Remove
listA.Remove(listA.Back())
//listA{-2,-1,0,1,2}
```

## func (\*List) Init

- Init initializes or clears list l.

```go
//func (l *List) Init() *List
listA = listA.Init()
//listA{}
```

# type Element

```go
type Element struct {

    // The value stored with this element.
    Value interface{}
    // contains filtered or unexported fields
}
```

## func (\*Element) Next & func (\*List) Front

- Next returns the next list element or nil.
- Back returns the last element of list l or nil if the list is empty.

```go
//func (e *Element) Next() *Element
for i:=-1;i<2;i++ {
    listA.PushBack(i)
    if i == 0 {
        element := listA.Back()
    }
}
//listA{-1,0,1}
//element == 0
println(elementl.Next())
println(elementl.Back())
//output:
//1
//-1
```
