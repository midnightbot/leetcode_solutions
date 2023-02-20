class DataStream:

    def __init__(self, value: int, k: int):
        self.q = []
        self.dicts = {}
        self.value = value
        self.k = k
        self.i = 0

    def consec(self, num: int) -> bool:
        self.q.append(num)
        self.i+=1
        self.dicts[num] = self.dicts.get(num,0)+1

        if self.i < self.k:
            return False

        else:
            if self.value in self.dicts and self.dicts[self.value] == self.k:
                self.dicts[self.q[self.i - self.k]]-=1
                return True

            else:
                self.dicts[self.q[self.i - self.k]]-=1
                return False


        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
