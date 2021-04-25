class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        
        mins = min(A)
        anss = [int(d) for d in str(mins)]
        sums = 0
        for x in range(len(anss)):
            sums+= anss[x]
            
        if sums%2!=0:
            return 0
        else:
            return 1
            
        
