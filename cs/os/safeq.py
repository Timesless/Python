"""
    线程安全的队列，用于实现线程池 与 任务队列
    Python同步原语：
        互斥量
            lock = threading.Lock()
            lock.acquire()
            lock.release()
        条件变量（信号量）：带有通知唤醒机制
            cond = threading.Condition()
            cond.acquire()
            cond.wait()
            cond.notify()
            cond.release()
"""

import threading
import time


class SafeQueue:

    # 构造函数，容量默认无穷大
    def __init__(self, maxlen=0):
        self.q = []
        self.cond = threading.Condition()
        self.maxlen = maxlen
        pass

    # 队列size
    def size(self):
        self.cond.acquire()
        size = len(self.q)
        self.cond.release()
        return size
        pass

    # 向安全队列中添加元素
    def put(self, item, timeout=2):

        # 添加元素时队列满则阻塞，默认两秒
        if self.maxlen != 0 and self.size() >= self.maxlen:
            self.cond.acquire()
            self.cond.wait(timeout=timeout)
            self.cond.release()
            if self.size() >= self.maxlen:
                raise Exception('队列已满')

        self.cond.acquire()
        self.q.append(item)
        # 有可能存在线程在pop时阻塞，这里添加后唤醒阻塞的线程
        self.cond.notify()
        self.cond.release()
        pass

    # 批量添加
    def put_batch(self, item_list):
        if not isinstance(item_list, list):
            item_list = list(item_list)
        for item in item_list:
            self.put(item)
        pass

    # 弹出一个元素
    def pop(self, timeout=2):
        if not self.size():
            self.cond.acquire()
            self.cond.wait(timeout=timeout)
            self.cond.release()

        # 加锁
        self.cond.acquire()
        if not len(self.q):
            return None
        item = self.q.pop()
        self.cond.notify()
        self.cond.release()
        return item
        pass

    # 获取指定idx的元素
    def get(self, idx):
        self.cond.acquire()
        item = self.q[idx]
        self.cond.release()
        return item
        pass


if __name__ == '__main__':
    q = SafeQueue()

    def producer():
        while True:
            for i in range(100):
                q.put(i)
                print(f'put into q: {i}\n')
                time.sleep(3)

    def consumer():
        while True:
            print("pop from q: {}".format(q.pop()))
            print(time.time())

    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    '''
        运行结果：
            put into q: 1
            pop from q: 1
            1603542448.438063
            pop from q: None
        生产者3s生产一个，消费者2s消费一个，消费者每消费一个都会消费到一个None
    '''

