class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        ans  = []
        low = 0
        high = len(numbers) - 1
        
        while high > low:
            if target == numbers[low] + numbers[high]:
                ans.append(low+1)
                ans.append(high+1)
                return ans
            
            elif numbers[low] + numbers[high] < target:
                low+=1
                
                
            else:
                high-=1
                
        ans.append(-1)
        ans.append(-1)
        return ans
                
                
        
                
                
            
                    
                
        
