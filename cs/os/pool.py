"""
任务处理线程
    停止，使用一个标记，标记线程何时停止
    事件循环，始终向任务队列中获取任务来执行
线程池
    包含一个或多个任务处理线程
    启动：启动任务处理线程
    停止：停止所有任务线程，并移除线程池中所有线程
    向线程池中提交任务
    批量提交任务
"""

import threading
import multiprocessing
from cs.os.task import Task, AsyncTask
from cs.os.safeq import SafeQueue


class ProcessThread(threading.Thread):
    def __init__(self, taskqueue: SafeQueue):
        # super().__init__()
        threading.Thread.__init__(self)
        # 任务队列
        self.taskqueue = taskqueue
        # 线程终止标记
        self.dismiss_flag = threading.Event()

    # 事件循环，始终向任务队列中获取任务来执行
    def run(self):
        while True:
            if self.dismiss_flag.is_set():
                break
            task = self.taskqueue.pop()
            # 如果任务队列中的元素不是Task类型则跳过
            if not isinstance(task, Task):
                continue
            # 如果任务函数为None则跳过
            if not task.call:
                continue
            # 执行函数调用
            result = task.call(*task.args, **task.kwargs)
            # 如果是异步任务，则应该设置其返回值
            if isinstance(task, AsyncTask):
                task.set_result(result)

    # 停止线程
    def stop(self):
        self.dismiss_flag.set()


# 线程池对象
class ThreadPool:
    def __init__(self, maxlen=0):
        # 默认 cpu 核数 * 2
        if not maxlen:
            maxlen = multiprocessing.cpu_count() << 1

        # 线程池
        self.pool: [ProcessThread] = SafeQueue(maxlen)
        # 任务队列，无界
        self.taskqueue: [Task] = SafeQueue()
        # 创建任务处理线程，放入线程池
        for i in range(maxlen):
            self.pool.put(ProcessThread(self.taskqueue))

    # 启动线程池，启动所有线程
    def start(self):
        for i in range(self.pool.size()):
            self.pool.get(i).start()

    # 停止线程池
    def shutdown(self):
        for i in range(self.pool.size()):
            self.pool.get(i).stop()
        while self.pool.size():
            cur_proccess = self.pool.pop()
            # 等待线程真正执行完毕
            cur_proccess.join()

    # 向线程池中提交任务
    def put(self, item):
        if not isinstance(item, Task):
            raise Exception('请提交正确的任务')
        self.taskqueue.put(item)

    def put_batch(self, item_list):
        if not isinstance(item_list, list):
            item_list = list(item_list)
        for item in item_list:
            self.put(item)

    def size(self):
        print(f"core thread count is: {self.pool.size()}, task queue remain: {self.taskqueue.size()}")
