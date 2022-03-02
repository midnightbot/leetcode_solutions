##ss
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.nums = set()
        for x in range(maxNumbers):
            self.nums.add(x)
            
        

    def get(self) -> int:
        if not self.nums:
            return -1
        else:
            return self.nums.pop()
        

    def check(self, number: int) -> bool:
        return number in self.nums
        

    def release(self, number: int) -> None:
        self.nums.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
