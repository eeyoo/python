### 知识点

1. Numbers
2. Strings - 字符串是字符的组合，可以通过下标确定
```Python
word = 'Python'
word[0] # character in position 0, aka 'P'
word[5] # character in position 5, aka 'n'
word[-1] # last character, aka 'n'
word[-2] # second-last character, aka 'o'
```
> Python strings cannot be changed — they are *immutable*.
3. Lists - 与字符串类似，但列表可以修改
```Python
squares = [1, 4, 9, 16, 25]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
```
内置函数`len()`可以获得列表变量的长度
