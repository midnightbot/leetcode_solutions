##ss
import heapq
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)
        prev = 0
        ans = 0
        #print(nums)
        indx = 0
        while k > 0 and indx < len(nums):
            top = nums[indx]
            #print(nums,ans,prev)
            ans = int(ans)
            if  top - prev  -1 >= 1:
                n = top - prev - 1
                
                if n <= k:
                    ans += n/2 * (2 * (prev+1) + (n-1) * 1)
                    ans = int(ans)
    
                    k-=n
                    prev = top
                    
                else:
                    n = k
                    ans += n/2 * (2 * (prev+1) + (n-1) * 1)
                    ans = int(ans)
                    k = 0
                    
            else:
                prev = top
                
            indx+=1
                    
        if k ==0:
            return int(ans)
        else:
            #print("ins",k,ans,prev)
            return int(ans + int((k/2) * (2*(prev+1) + (k-1)*1)))
        
