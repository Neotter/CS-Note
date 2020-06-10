<!--
 * @Author: Nettor
 * @Date: 2020-06-10 13:46:56
 * @LastEditors: Nettor
 * @LastEditTime: 2020-06-10 14:38:38
 * @Description: file content
-->

# What is the difference between String, StringBuffer and StringBuild

In general, String class uses the `final` keyword to an character array to hold a string. `private final char value[]`, so `String` is immutable.

The "immutable" means the content of a string in memory can't be changed.
However, the content of a String object cannot be modified, but that doesn't mean its reference can't be changed.
Every time change a string like this.

```java
public class JavaTest {
	public static void main(String[] args) {
		String str = "Hello";
		str = str + " World";
		System.out.println("str=" + str);
	}
}
```

It will allocated a new space of memory to replace the old one.

> After Java 9, the implement of String class use byte array to store string `private final byte[] value`;

`StringBuild` and `StringBuffer` all extend from `AbstractBuilder`, `AbstractStringBuilder` also uses `char[] value` to hold string but doesn't have `final` keyword, so `StringBuild` and `StringBuffer` are alterable.

```java
abstract class AbstractStringBuilder implements Appendable, CharSequence {
    /**
     * The value is used for character storage.
     */
    char[] value;

    /**
     * The count is the number of characters used.
     */
    int count;

    AbstractStringBuilder(int capacity) {
        value = new char[capacity];
    }}
```

## Thread safety

`String` is immutable, it is thread safety.

`StringBuffer` has `synchronized` keyword, it is thread safety too.

`StringBuilder` doesn't have `synchronized` keyword, it is thread unsafety

## Performance

Every you change a `String` instance, it will generate a new String instance, then the pointer point to new String instance, `StringBuilder` and `StringBuffer` change the instance itself.

Using `StringBuilder` in the same situation will only improve performance by about 10%-15% compared to using `StringBuffer`, but you run the risk of multi-threading insecurity.

## Summary

1. Manipulate small amounts of data: `String`

2. Manipulate large amounts of data in a single-threaded string buffer: `StringBuilder`

3. Manipulate large amounts of data in a mutil-threaded string buffer: `StringBuffer`
