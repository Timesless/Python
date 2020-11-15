

# LFU Node类

from cs.computer_principle.DoubleLinkedList import DoubleLinkedList, Node


class LFUNode(Node):

    def __init__(self, item, freq=0):
        self.freq = freq
        super().__init__(item)


class LFUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = {}
        sel
