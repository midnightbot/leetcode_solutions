class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        temp = []
        prev = 0
        
        for x in nums:
            if x == 0:
                prev+=1
                    
            else:
                if prev!=0:
                    temp.append(prev)
                prev = 0
            
        if prev!=0:
            temp.append(prev)
            
        return sum([x*(x+1)//2 for x in temp])
