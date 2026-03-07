class Solution:
    def find_reverse(self, n:int) -> int:
        temp = [x for x in str(n)]
        temp = temp[::-1]
        temp = "".join(temp)
        return int(temp)

    def mirrorDistance(self, n: int) -> int:
        return abs(n-self.find_reverse(n))
        
