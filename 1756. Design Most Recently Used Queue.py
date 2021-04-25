class MRUQueue:

    def __init__(self, n: int):
        self.nums = list(range(1, n+1))
        

    def fetch(self, k: int) -> int:
        n = self.nums.pop(k-1)
        self.nums.append(n)
        return n
        
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
