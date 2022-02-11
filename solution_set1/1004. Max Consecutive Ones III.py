##ss
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        if k == 0:
            ans = 0
            thisans = 0
            for x in range(len(nums)):
                if nums[x] == 1:
                    thisans+=1
                    
                else:
                    ans = max(ans,thisans)
                    thisans = 0
            ans = max(ans,thisans)       
            return ans
        maxlen = 0
        past = []
        thislen = 0
        start = 0
        for x in range(len(nums)):
            #print(thislen,past)
            if nums[x] ==1:
                thislen+=1
                
            elif nums[x] == 0 and k > 0:
                thislen+=1
                past.append(x)
                k-=1
                
            elif nums[x] == 0 and k == 0:
                indx = past.pop(0)
                thislen-= (indx - start)
                start = indx+1
                thislen = (x - start + 1)
                past.append(x)
            maxlen = max(maxlen,thislen)
            
        return maxlen
                
            
        
