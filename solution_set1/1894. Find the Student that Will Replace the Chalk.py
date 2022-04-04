##ss
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        sums = sum(chalk)
        
        l = 0
        r = k//sums + 1
        
        while l < r: ## instead of finding linearly how many times to subtract the sum, use binary search to do it
            #print(l,r)
            mid = (l+r) // 2
            
            if sums * mid > k:
                r = mid
            
            else:
                l = mid + 1
                
        #print(l,r)
        k-= sums*(l-1)
        #print(k)
        pos = 0
        while k >= 0:
            if chalk[pos] <= k:
                k-=chalk[pos]
                pos+=1
                
            else:
                return pos
                
        
