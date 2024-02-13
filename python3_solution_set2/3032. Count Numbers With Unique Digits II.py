class Solution:
    def numberCount(self, a: int, b: int) -> int:
        ans = 0
        for x in range(a, b+1):
            num = [i for i in str(x)]
            numset = set(num)
            if len(num) == len(numset):
                ans+=1
                
        return ans
        
