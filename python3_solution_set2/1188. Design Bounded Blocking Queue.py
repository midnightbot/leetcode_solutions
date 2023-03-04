import threading
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.q = []
        self.capacity = capacity
        self.push_lock = threading.Semaphore(capacity)
        self.pop_lock = threading.Semaphore(0)
        self.edit = threading.Lock()

        

    def enqueue(self, element: int) -> None:
        self.push_lock.acquire()
        self.edit.acquire()
        self.q.append(element)
        self.edit.release()
        self.pop_lock.release()


    def dequeue(self) -> int:
        self.pop_lock.acquire()
        self.edit.acquire()
        top = self.q.pop(0)
        self.edit.release()
        self.push_lock.release()
        return top

    def size(self) -> int:
        return len(self.q)
