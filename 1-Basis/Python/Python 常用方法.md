# 数据格式

## 字符串 string

|Method|	Description|
|---|---|
|capitalize()|	Converts the first character to upper case|
|casefold()|	Converts string into lower case|
|center()|	Returns a centered string|
|count()|	Returns the number of times a specified value occurs in a string|
|encode()|	Returns an encoded version of the string|
|endswith()|	Returns true if the string ends with the specified value|
|expandtabs()|	Sets the tab size of the string|
|find()|	Searches the string for a specified value and returns the position of where it was found|
|format()|	Formats specified values in a string|
|format_map()|	Formats specified values in a string|
|index()|	Searches the string for a specified value and returns the position of where it was found|
|isalnum()|	Returns True if all characters in the string are alphanumeric|
|isalpha()|	Returns True if all characters in the string are in the alphabet|
|isascii()|	Returns True if all characters in the string are ascii characters|
|isdecimal()|	Returns True if all characters in the string are decimals|
|isdigit()|	Returns True if all characters in the string are digits|
|isidentifier()|	Returns True if the string is an identifier|
|islower()|	Returns True if all characters in the string are lower case|
|isnumeric()|	Returns True if all characters in the string are numeric|
|isprintable()|	Returns True if all characters in the string are printable|
|isspace()|	Returns True if all characters in the string are whitespaces|
|istitle()|	Returns True if the string follows the rules of a title|
|isupper()|	Returns True if all characters in the string are upper case|
|join()|	Converts the elements of an iterable into a string|
|ljust()|	Returns a left justified version of the string|
|lower()|	Converts a string into lower case|
|lstrip()|	Returns a left trim version of the string|
|maketrans()|	Returns a translation table to be used in translations|
|partition()|	Returns a tuple where the string is parted into three parts|
|replace()|	Returns a string where a specified value is replaced with a specified value|
|rfind()|	Searches the string for a specified value and returns the last position of where it was found|
|rindex()|	Searches the string for a specified value and returns the last position of where it was found|
|rjust()|	Returns a right justified version of the string|
|rpartition()|	Returns a tuple where the string is parted into three parts|
|rsplit()|	Splits the string at the specified separator, and returns a list|
|rstrip()|	Returns a right trim version of the string|
|split()|	Splits the string at the specified separator, and returns a list|
|splitlines()|	Splits the string at line breaks and returns a list|
|startswith()|	Returns true if the string starts with the specified value|
|strip()|	Returns a trimmed version of the string|
|swapcase()|	Swaps cases, lower case becomes upper case and vice versa|
|title()|Converts the first character of each word to upper case|
|translate()|	Returns a translated string|
|upper()|	Converts a string into upper case|
|zfill()|	Fills the string with a specified number of 0 values at the beginning|

1. **str()** 转换为字符串
2. **str1 + str2** 对多个字符串进行拼接
3.  **len(str1)** 计算字符串的长度
4. **string[start : end : step]**  字符串切片
5. **str.split(sep, maxsplit)** 分割字符串 **maxsplit**:可选参数,用于指定分割的次数,如果不指定或者为-1,则分割次数没有限制,否则返回结果列表的元素个数最多为 maxsplit+1
6. 检索字符串
   1. **count()方法** `str.count(substr, start, end)` 用于检索指定字符串在另一个字符串中出现的次数，如果检索的字符串不存在则返回0，否则返回出现的次数。
   2. **find()方法** `str.find(substr, start, end)`作用：检索是否包含指定的字符串，如果检索的字符串不存在则返回-1，否则返回首次出现该字符串时的索引。
   3. **index()方法** `str.index(substr, start, end)`作用：和find方法类似，也用于检索是否包含指定的字符串，使用index方法，当指定的字符串**不存在时会抛异常**。
7. **去除字符串中的空格和特殊字符**
   1. **strip()方法** `str.strip([chars])`去除字符串前后（左右侧）的空格或特殊字符
   2. **lstrip()方法** 去除左侧
   3. **rstrip()方法** 去除右侧
8. 字符串转换为列表 `list2 = list(map(str.split().split())`

## 元组 tuple

...

## 字典 dict
|Method|	Description|
|---|---|
clear()|	Removes all the elements from the dictionary
copy()|	Returns a copy of the dictionary **深拷贝**
fromkeys()|	Returns a dictionary with the specified keys and value
get()|	Returns the value of the specified key，不存在返回None
items()|	Returns a list containing a tuple for each key value pair
keys()|	Returns a list containing the dictionary's keys
pop()|	Removes the element with the specified key
popitem()|	Removes the last inserted key-value pair
**setdefault()**|	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()|	Updates the dictionary with the specified key-value pairs
values()|	Returns a list of all the values in the dictionary
## 列表 list
|Method|	Description|
|---|---|
append()|	Adds an element at the end of the list
clear()|	Removes all the elements from the list
copy()|	Returns a copy of the list
count()|	Returns the number of elements with the specified value
extend()|	Add the elements of a list (or any iterable), to the end of the current list
index()|	Returns the index of the first element with the specified value
insert()|	Adds an element at the specified position
pop()|	Removes the element at the specified position
remove()|	Removes the first item with the specified value
reverse()|	Reverses the order of the list
sort()|	Sorts the list

**增加**

1. **list.append()** 增加元素
2. **list.extend(list2)** 扩展列表
3. **list.insert(-1,[a1,a2])** 在指定索引位置的前面插入元素
4. **list2 = list.copy()** 拷贝

**删除**

1. **list.index(a1,a2,a3)** 根据值获取当前值索引位置（左边优先，找到后就不会找下一个元素了）
2. **list.pop(2)** 删除某个值(1.指定索引；2. 默认最后一个)，并获取删除的值
3. **li.remove(a1)** 删除列表中的指定值 只能删除一个
4. **list.clear()** 清空
5. 列表中删除元素(索引删除和切片删除) del li[2]  del li[0:2]

**检索、排序、翻转**

1. **li.reverse()** 将当前列表进行翻转
2. **li.sort()** 列表的排序（reverse=True时倒序排序）
3. **list.count()** 统计次数
4. 列表中的in操作(返回布尔值真与假)
5. 列表转换成字符串（a.直接使用字符串join方法：列表中的元素只有字符串 b.需要自己写for循环一个一个处理： 既有数字又有字符串）


## 集合 set 

|Method|	Description|
|---|---|
add()|	Adds an element to the set
clear()|	Removes all the elements from the set
copy()|	Returns a copy of the set
difference()|	Returns a set containing the difference between two or more sets
difference_update()|	Removes the items in this set that are also included in another, specified set
discard()|	Remove the specified item
intersection()|	Returns a set, that is the intersection of two or more sets
intersection_update()|	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()|	Returns whether two sets have a intersection or not
issubset()|	Returns whether another set contains this set or not
issuperset()|	Returns whether this set contains another set or not
pop()|	Removes an element from the set
remove()|	Removes the specified element
symmetric_difference()|	Returns a set with the symmetric differences of two sets
symmetric_difference_update()|	inserts the symmetric differences from this set and another
union()|	Return a set containing the union of sets
update()|	Update the set with another set, or any other iterable

# 操作

## 遍历

## 切片

# 输入/输出
**输入**
使用 `input` 输入的都是 `str` 格式
```python
val = input("please input val")
num1 = int(input())
num2 = float(input())
```
使用 `split` 方法多输入
```python
input().split(separator, maxsplit)
x = list(map(int, input().split())) # x 是一个int类型的list
x, y = input().split()
x,y = [int (x) for x in input().split()]
```
**输出**
使用 `print` 方法
```python

# end 参数
for i in range(2):
		print(i, end = '>>>') # 0>>>1>>>
# sep 参数
print('09','12','2016',sep = '-') # 09-12-2016
		
```
对 output 进行 format
```python
print(f"{augument}") # python3

# Python program showing
# a use of format() method

# combining positional and keyword arguments
print('Number one portal is {0}, {1}, and {other}.'
	.format('Geeks', 'For', other ='Geeks'))
# Number one portal is Geeks, For, and Geeks.

# using format() method with number
print("Geeks :{0:2d}, Portal :{1:8.2f}".
	format(12, 00.546))
#Geeks :12, Portal :    0.55

# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".
	format(47.42, 11))
#Second argument:  11, first one:   47.42

print("Geeks: {a:5d}, Portal: {p:8.2f}".
	format(a = 453, p = 59.058))
#Geeks:   453, Portal:    59.06

print("My name is {:>10}.".format("Jane")) # >表示右对齐，10个字符位，不满用空格填满
```

