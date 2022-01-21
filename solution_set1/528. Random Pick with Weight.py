##ss
import random
import math
##python weighted random pick : https://pynative.com/python-weighted-random-choices-with-probability/
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.weights = []
        sums = sum(w)
        for x in range(len(w)):
            self.weights.append(w[x]/sums)
            
        self.indx = [x for x in range(len(w))]

    def pickIndex(self) -> int:
        return random.choices(self.indx,weights = self.weights,k=1)[0]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
