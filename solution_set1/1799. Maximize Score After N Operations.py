##Solution 1 (75/76 test cases passed TLE)
import math
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums) // 2
        
        @lru_cache(None)
        def findgcd(x,y):
            return math.gcd(x,y)
        
        def tostring(arr):
            strs = ""
            
            for x in range(len(arr)):
                if x == len(arr) - 1:
                    strs+=str(arr[x])
                else:
                    strs+= str(arr[x]) + ","
                    
            return strs
        
        def toarr(strs):
            return strs.split(",")
        
        @lru_cache(None)
        def max_ans(left,i):
            
            if i == n:
                indx = []
                comp = left.split(',')
                for x in range(len(comp)):
                    if comp[x] == '0':
                        indx.append(x)
                        
                return i * findgcd(nums[indx[0]],nums[indx[1]])
                
            else:
                
                comp = left.split(',')
                ans = -1
                for x in range(len(comp)-1):
                    for y in range(x+1,len(comp)):
                        if comp[x] == '0' and comp[y] == '0':
                            comp[x] = '1'
                            comp[y] = '1'
                            thisans = i * findgcd(nums[x],nums[y]) + max_ans(tostring(comp),i+1)
                            comp[x] = '0'
                            comp[y] = '0'
                            
                            ans = max(ans,thisans)
                return ans
                            
                        
                
        return max_ans(','.join(['0' for x in range(n*2)]),1)
