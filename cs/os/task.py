import uuid
import threading


# 基本任务对象
class Task:

    def __init__(self, func, *args, **kwargs):
        self.id = uuid.uuid4()
        # 任务的具体逻辑，通过函数引用传递
        self.call = func
        # 任务的元组、字典参数
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return f'task id: {self.id}'


# 异步任务对象
class AsyncTask(Task):
    def __init__(self, func, *args, **kwargs):
        super().__init__(func, *args, **kwargs)
        self.result = None
        # 设置值的时候需要同步
        self.cond = threading.Condition()

    # 设置异步任务的执行结果
    def set_result(self, result):
        self.cond.acquire()
        self.result = result
        self.cond.notify()
        self.cond.release()

    # 获取异步任务的执行结果
    def get_result(self):
        self.cond.acquire()
        if not self.result:
            self.cond.wait()
        result = self.result
        self.cond.release()
        return result


# 测试
if __name__ == '__main__':
    def test_func():
        print('this is a task test')


    task = Task(func=test_func)
    print(task)
