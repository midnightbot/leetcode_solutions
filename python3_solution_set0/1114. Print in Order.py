class Foo:
    def __init__(self):
        self.s1 = threading.Semaphore(0)
        self.s2 = threading.Semaphore(0)


    def first(self, printFirst: 'Callable[[], None]') -> None:
       
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.s1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.s1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.s2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.s2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
