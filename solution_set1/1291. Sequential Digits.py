##ss
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        ans = '123456789'
        
        result = []
        
        l1 = len(str(low))
        l2 = len(str(high))
        
        for x in range(l1,l2+1):
            
            for y in range(9-x+1):
                temp = int(ans[y:y+x])
                
                if temp >= low and temp <=high:
                    result.append(temp)
                    
                    
        return result
