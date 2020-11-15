"""
初始化线程池
启动
提交任务
终止
"""
import time
from cs.os.pool import ThreadPool
from cs.os.task import Task, AsyncTask


def test():
    # 任务执行具体逻辑
    def logic():
        print('this is a simple task: 1')
        time.sleep(1)
        print('this is a simple task: 2')
    pool = ThreadPool()
    pool.start()
    for i in range(10):
        pool.put(Task(func=logic))

    time.sleep(2)
    pool.shutdown()


def test_async():

    def logic():
        time.sleep(2)
        return sum(range(101))
    pool = ThreadPool()
    pool.start()

    lt: [AsyncTask] = []
    for i in range(1):
        task = AsyncTask(func=logic)
        lt.append(task)
        pool.put(task)
        print("execute task...")
    # 阻塞等待获取结果
    for asynctask in lt:
        print('{} rs is: {}'.format(str(asynctask), asynctask.get_result()))

    time.sleep(3)
    pool.size()
    pool.shutdown()
    pool.size()


if __name__ == '__main__':
    # test()
    test_async()
