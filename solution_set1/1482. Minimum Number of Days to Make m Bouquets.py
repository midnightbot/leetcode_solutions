##ss
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        l = 1
        r = max(bloomDay)
        
        if m * k > len(bloomDay):
            return -1
        def can_do(day):
            done = 0
            temp = 0
            for x in bloomDay:
                temp = 0 if x > day else temp + 1
                if temp >= k:
                    temp = 0
                    done+=1
                    
                    if done == m:
                        break
                        
            return done>=m
        
        
        while l < r:
            mid = (l+r) // 2
            
            if can_do(mid):
                r = mid
                
            else:
                l = mid + 1
                
        return l
                
                
                
        
