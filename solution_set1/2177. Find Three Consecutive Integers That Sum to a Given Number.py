##ss
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        ## x-1  x  x+1 be the 3 numbers
        
        if num%3!=0:
            return []
        
        else:
            x = num // 3
            
            return [x-1,x,x+1]
        
