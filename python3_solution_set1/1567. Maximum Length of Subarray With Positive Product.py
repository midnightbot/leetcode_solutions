##ss
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        arr = []
        thisarr = []
        
        ##split array at 0's
        ## find max len of pos product in these subarrays now
        
        ##if count(neg)%2==0: ans = max(ans, full-length-subarray)
        ##else: ans = max(ans, subarray[0:last-negative-pos], subarray[first_neg-pos+1:])
        for x in nums:
            if x == 0:
                if len(thisarr)!=0:
                    arr.append(thisarr)
                    
                thisarr = []
            else:
                thisarr.append(x)
                
        arr.append(thisarr)
        
        ans = 0
        
        for x in range(len(arr)):
            pos = {'first':0, 'last':0}
            count = 0
            
            for y in range(len(arr[x])):
                if arr[x][y] < 0 and count ==0:
                    count+=1
                    pos['first'] = y
                    pos['last'] = y
                    
                elif arr[x][y] < 0 and count > 0:
                    count+=1
                    pos['last'] = y
                    
                    
            if count%2==0:
                ans = max(ans, len(arr[x]))
                
            else:
                ans = max(ans, len(arr[x][0:pos['last']]), len(arr[x][pos['first']+1:]))
                
                
        return ans
