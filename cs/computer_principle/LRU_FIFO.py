"""

缓存置换 - FIFO

"""

from cs.computer_principle.DoubleLinkedList import DoubleLinkedList


class FIFO:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.list = DoubleLinkedList(capacity)

    def get(self, key):
        if key in self.map:
            return self.map[key]
        return -1

    # ==========================================
    # LRU 实现
    # ==========================================

    def put(self, key, value):
        val = value
        if key not in self.map:
            # 缓存满，置换最先进入的元素
            if self.size >= self.capacity:
                val = self.list.pop_front()
                del self.map[val]
                self.list.append(key)
            # 新增
            else:
                self.size += 1
                self.list.append(key)
        # 修改时，返回原来节点的值
        else:
            val = self.map[key]

        self.map[key] = value
        return val

    # 约定：队头为热点数据，队尾为最近最久未使用的数据
    def get_lru(self, key):
        if key not in self.map:
            return -1
        # 访问一次的节点，放到队头
        self.list.remove(key)
        self.list.append_front(key)

        return self.map[key]

    def put_lru(self, key, value):
        val = value
        if key not in self.map:
            # 缓存满，置换最少使用的，即队尾的
            if self.size >= self.capacity:
                # 删除队尾元素
                val = self.list.pop()
                del self.map[val]
            # 新增
            else:
                self.size += 1
        # 修改值
        else:
            val = self.map[key]

        # 访问的时候先删除，再添加到队首
        self.map[key] = value
        self.list.remove(key)
        self.list.append_front(key)

        return val

    def print(self):
        print(self.map)


def fifo_test():
    cache = FIFO(2)
    print(cache.get(1))
    cache.put(1, 1)
    cache.put(1, 2)
    cache.print()
    cache.put(2, 2)
    cache.print()
    cache.put(2, 3)
    cache.print()
    print(cache.put(3, 3))
    cache.print()
    print(cache.get(1))


def lru_test():
    cache = FIFO(2)
    print(cache.get_lru(1))
    cache.put_lru(1, 1)
    cache.print()
    cache.put_lru(2, 2)
    cache.print()
    cache.put_lru(2, 3)
    cache.print()
    cache.put_lru(1, 2)
    cache.print()
    print(cache.put_lru(3, 3))
    cache.print()
    print(cache.get_lru(1))
    print(cache.get_lru(2))
    cache.put_lru(4, 4)
    cache.print()


if __name__ == '__main__':
    fifo_test()
    print(' =============== ')
    lru_test()


