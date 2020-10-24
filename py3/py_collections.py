
"""
collections -- 容器数据类型，

ChainMap 将多个集合映射到一个视图，效率高于 update

Counter: 提供可哈希对象的激素功能

deque：双端队列，实现两端添加和弹出为O1

namedtuple() 创建命名元组子类的工厂函数

OrderDict

deaultdict

UserDict

UserList

UserString
"""
import os

dirs = os.walk(r"D:\test")
for path, dir_list, file_list in dirs:
    dir_name = str(dir_list)
    if dir_name == '.git' or dir_name == 'assets':
        continue
    for file_name in file_list:
        cf = open(os.path.join(path, file_name), "r+", encoding='utf-8')
        content = cf.read()
        print(content)
        if content.find('image-') < 0:
            cf.close()
            continue

        cf.seek(0)
        cf.write(content)
        cf.close()

