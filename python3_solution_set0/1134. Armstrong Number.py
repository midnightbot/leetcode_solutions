class Solution:
    def isArmstrong(self, n: int) -> bool:
        
        res = [int(x) for x in str(n)]
        count = len(res)
        sums = 0
        for x in range(len(res)):
            sums+=pow(res[x],count)
            
        if sums==n:
            return True
        else:
            return False
        
