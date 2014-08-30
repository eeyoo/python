### 控制流

if语句
----
```Python
x = int(raw_input("Please enter an integer: "))
if x < 0:
		x = 0
		print 'Negative changed to zero'
	elif x == 0:
		print 'Zero'
	elif x == 1:
		print 'Single'
	else:
		print 'More'
		
```

for语句
----
1. 计算字符串列表单元的长度
```Python
words = ['cat', 'window', 'defenestrate']
for w in words:
	print w, len(w)
	
cat 3
window 5
defenestrate 12
```
2. 使用内置函数`range()`获得数值列表
```Python
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print i, a[1]
	
0 Mary
1 had
2 a
3 little
4 lamb
```
break, continue语句，以及else与循环语句的配合
--------

1. break - break会中断最小的循环体
```Python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, '=', x, '*', n/x
            break
    else:
        print n, 'is a prime number'
```
注意，else并非与if语句配合使用，而是与内部for语句配合使用。
这里，有个隐性知识。range(2,2)是一个空列表，for语句不会执行空列表的单元，而是跳到
else语句执行。以上是找到2-10(不包含10)范围中的素数。
用基本的控制流达到特定的目标，就是算法的体现。
算法不是遥不可及的东西，细心发现，一定有收获。

2. continue - 终止当前循环，继续下一次循环
```Python
for num in range(2, 10):
    if num % 2 == 0:
        print "Found an even number", num # even number - 偶数
        continue
    print "Found a odd number", num  # odd number - 奇数
	
```
如果将continue换成break，只能循环一次。

pass语句
-------------
表示空操作，例如
```Python 
while True:
	pass # 循环等待中断指令(Ctrl+C)
	
```

```Python 
class MyEmptyClass:
	pass # 最小的类
	
```

```Python 
def initlog(*args):
	pass # 等待进一步实现函数体
	
```

函数定义
---------
关键字def定义函数，函数体需要缩进。函数的符号表问题，默认的返回值(None)，以及确定的返回值类型。
函数定义的规范性是函数体首行`"""..."""`文档，是函数的说明文档。

函数定义的扩展
-----------
函数可以不止一个参数，最实用是定义参数的默认值。
```Python
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint
		
```
三种调用方式：
* ask_ok('Do you really want to quit?')
* ask_ok('OK to overwrite the file?', 2)
* ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


