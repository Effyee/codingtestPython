class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.full = k 

    def enQueue(self, value: int) -> bool:
        if len(self.queue) != self.full:
            self.queue.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if len(self.queue) == 0:
            return False
        self.queue.pop(0)
        return True

    def Front(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[0]

    def Rear(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.full