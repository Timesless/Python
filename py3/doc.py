"""
# 遍历字典
for k, v in dt.items()

# 携带索引遍历列表
for i, v in enumerate(['1', '2', '3'])
"""

# zip()遍历多个序列
question = ['name ?', 'quest ?', 'color ?']
answer = ['yangzl', 'the holy', 'cyan']
for q, a in zip(question, answer):
    print(f"q is : {q}, a is {a}")

"""
# 创建文件
f = open("./foo.txt", "w+")
f.write("hello, python3\nhello file")
f.flush()
f.close()

# read()
# readline
# readlines()
f = open("./foo.txt", "w+")
lt = f.readlines()
for i, v in lt:
    print(v)

seek()
seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符
"""

"""
Python3 内置函数
"""
print(abs(-5))

# dict(**kwarg)
# dict(mapping, **kwarg)
# dict(iterable, **kwarg)

print(dict(a='a', b='b', c='c'))
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))

# 查看帮助信息
# help('str')

lt = list((1, 5, 6, 7, 0))

# max / min / round()
print(max(lt))
print(min(lt))


# getattr / setattr / hasattr / delattr
class Coordinate:
    x = 10
    y = -5
    z = 0


print('----------------------------')
p1 = Coordinate()
print(hasattr(p1, 'x'))
print(getattr(p1, 'x'))
setattr(p1, 'x', 20)
delattr(Coordinate, 'z')
print('x = ', p1.x, 'y = ', p1.y)
print('----------------------------')

# all / any , 判断元素是否有空，0，false
print(all(lt))
print(any(lt))

print(dir(lt))

# 16进制、8进制、二进制
print(hex(255), oct(255), bin(255))

print(next(iter(lt)))

print(lt[slice(2)])
print(lt)

# divmod，返回一个包含商和余数的元组(a // b, a % b)
print(divmod(3.0, 1.3))

# cPython取对象地址
print(id(lt))

# sort / sorted sort用于list，sorted用在所有可迭代对象
print(sorted({1: 'D', 2: 'B', 3: 'C'}, key=lambda x: x * -1))

# enumerate，将一个可便利数据对象（列表、元组、字符串）组合为一个索引序列
for i, v in enumerate(lt):
    print(i, end=" ")

# @staticmethod，在类中通过该注解标明静态方法
# @classmethod: 注解的函数不需要实例化，不需要self参数，第一个参数是表示自身类的cls

# eval，执行字符串表达式并返回值
# exec，能传入全局变量与局部变量，exec(object[, globals][, locals])
print(eval('pow(2, 2) + 40'))

# type / isinstance isinstance认为子类型是父类型，type不考虑继承关系
# issubclass(class, targetclass)，判断class是否targetclass的子类
print(isinstance(True, int))
print(type(True) == int)

# sum(iterable[, start])    start默认为零，所有可迭代对象做参数
print(sum({1: 'D', 2: 'B', 3: 'C'}, 0))

"""
bytearray，返回一个字节数组，数组元素可变，且每个元素范围 0 <= x <- 255
class bytearray([source[, encoding[, errors]]])
如果 source 为整数，则返回一个长度为 source 的初始化数组；
如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
如果没有输入任何参数，默认就是初始化数组为0个元素。

class bytes([source[, encoding[, errors]]])
是bytearray的不可变版本
"""
print(bytearray(lt))
print(bytes(lt))

# filter(function, iterable)
print(list(filter(lambda x: x < 5, lt)))

# pow(x, y[, z])，如果参数z存在，则是模幂运算
# math.pow()把参数转换为float，内置函数把参数做为整型
print("模幂运算的结果是：{}".format(pow(2, 3, 5)))

# super() 调用父类方法，涉及 MRO(方法解析顺序表)，重复调用(Diamond 继承)等问题
# super(type[, object-or-type]), Python 3可直接使用super().xxx()
print(super(int).__dir__())

'''
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
sep -- 用来间隔多个对象，默认值是一个空格。
end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
file -- 要写入的文件对象。
flush -- 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新。
'''

# callable() 检查对象是否可调用，返回True仍然可能调用失败
print(callable(lt))

# 不可变集合
print(frozenset(lt))

# range(start, stop[, step])
# start 起始， stop 截止， step 步长默认1

# vars([object]) 返回object对象的属性和属性值的字典对象
print(vars(dict))

# locals() 以字典类型返回当前位置所有的局部变量
# globals() 以字典类型返回当前位置所有的全局变量
print(locals())

# map(function, iterable, ...)
print(tuple(map(lambda x: x ** 2, lt)))

# reversed(seq) 以迭代器返回要转换的序列的倒叙（tuple, string, list, range）
print(tuple(reversed(lt)))

# __import__() 动态加载类和函数， __import__(name[, globals[, locals[, fromlist[, level]]]])

# class complex(real[, imag])
print(complex(1, 2))

# hash(object)，object为字符串 / 数值
print(hash('lt'))

# momeryview，返回元组列表
print(memoryview(bytearray('abcd', 'utf-8')))


# from collections import ChainMap

print('<img src="image-2020"'.replace('image-', './asset/image-'))
