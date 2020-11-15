"""
双向链表
参照JDK实现，为什么呢，因为我感觉JDK的双向链表写的贼好
作为缓存置换算法的链表类

1 从头部添加节点
2 从尾部添加节点
3 添加任意节点

4 从头部删除节点
5 从尾部删除节点
6 删除任意节点

FIFO 节点类，缓存满时只需置换最先进入队列的数据

LRU 节点类，每次get，put都应该将当前数据置为热点数据

LFU 节点类，需要保存访问的频次
"""


class DoubleLinkedList:
    def __init__(self, capacity=0x0fffffff):
        self.head = self.tail = None
        # 最大容量
        self.capacity = capacity
        # 当前容量
        self.size = 0

    #
    # 提供给用户的接口
    #

    def pop(self):
        return self.__poplast()

    def pop_front(self):
        return self.__popfirst()

    def remove(self, val):
        return self.__popnode(val)

    def append(self, val):
        self.__linklast(val)

    def append_front(self, val):
        self.__linkfirst(val)

    def print(self):
        if not self.head:
            return ''
        p = self.head
        line = ''
        while p.next:
            line += '%s <=> ' % p
            p = p.next
        if p:
            line += '%s ' % p
        print(line)

    #
    # 内部实现
    #

    # 从头部添加节点
    def __linkfirst(self, val):
        first = self.head
        new = Node(val, None, first)
        self.head = new
        # 如果头节点为空
        if not first:
            self.tail = new
        else:
            first.prev = new
        self.size += 1
        return new

    # 从尾部添加节点
    def __linklast(self, val):
        last = self.tail
        new = Node(val, last, None)
        self.tail = new
        # 如果尾节点为空
        if not last:
            self.head = new
        else:
            last.next = new
        self.size += 1
        return new

    # find
    def __findnode(self, val):
        if not self.head:
            return None
        p = self.head
        while p:
            if p.val == val:
                return p
            p = p.next
        return None

    # pop
    def __popnode(self, val):
        node = self.__findnode(val)
        if not node:
            return None
        if node == self.head:
            self.__popfirst()
        elif node == self.tail:
            self.__poplast()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.size -= 1
        return val

    def __popfirst(self):
        if not self.head:
            return None
        first = self.head
        if first.next:
            self.head = first.next
            # 将新的头节点的前驱置为None，那么就没有引用指向原头节点，会被GC
            self.head.prev = None
        else:
            self.head = self.tail = None
        return first.val

    def __poplast(self):
        if not self.tail:
            return None
        last = self.tail
        if last.prev:
            self.tail = last.prev
            # 将新头节点的后继置为None，那么就没有引用指向原尾节点，会被GC
            self.tail.next = None
        else:
            self.head = self.tail = None
        return last.val

    # pop_last
    # def __poplast(self):
    #     if not self.tail:
    #         return None
    #     last = self.tail
    #     new_tail = last.prev
    #
    #     # 清理资源
    #     val = last.val
    #     last.val = None
    #     last.prev = None
    #
    #     # 设置新的尾节点
    #     self.tail = new_tail
    #     # 如果新的尾节点为None，那么head节点也置为None
    #     if not new_tail:
    #         self.head = None
    #     else:
    #         new_tail.next = None
    #
    #     self.size -= 1
    #     return val

    # pop_first
    # def __popfirst(self):
    #     if not self.head:
    #         return None
    #
    #     first = self.head
    #     new_first = first.next
    #
    #     # 清理资源
    #     val = first.val
    #     first.next = None
    #     first.val = None
    #
    #     self.head = new_first
    #     if not new_first:
    #         self.tail = None
    #     else:
    #         new_first.prev = None
    #
    #     self.size -= 1
    #     return val


# 节点类， 个人感觉不用存k，v，只需要存k就行了
class Node:

    # 重载 构造器
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    # 覆写__str__
    def __str__(self):
        return '{ %s }' % self.val


# LRU 节点类，每次get，put都应该将当前数据置为热点数据

# LFU 节点类，需要保存访问的频次


if __name__ == '__main__':
    lt = DoubleLinkedList()
    for i in range(10):
        lt.append(i)
    lt.print()

    lt.remove(4)
    lt.remove(7)
    lt.print()
    lt.append_front(4)
    lt.print()
    lt.pop()
    lt.print()
    lt.pop_front()
    lt.print()
    lt.remove(6)
    lt.print()
