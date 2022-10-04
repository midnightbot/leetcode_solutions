##ss
class Solution:
    def countEven(self, num: int) -> int:
        
        ans = 0
        
        for x in range(1,num+1):
            
            comp = [int(z) for z in str(x)]
            if sum(comp)%2==0:
                ans+=1
                
        return ans
        
