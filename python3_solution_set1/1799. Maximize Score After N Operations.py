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

    
  ## Solution 2 (Same as above, just use bitmask instead of string)

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        n = len(nums) // 2
        
        @lru_cache(None)
        def findgcd(x,y):
            return math.gcd(x,y)
        
        
        @lru_cache(None)
        def solve(left,i):
            
            if i == n + 1:##base case
                return 0
            
            else:
                ans = -1
                
                for x in range(2*n):
                    if(left >> x) & 1:
                        continue
                        
                    for y in range(x+1,2*n):
                        if (left >> y) & 1:
                            continue
                            
                        thisscore = i * findgcd(nums[x],nums[y]) + solve(left | (1 << x) | (1<<y),i+1)
                        
                        ans = max(ans, thisscore)
                        
                return ans
            
            
            
            
            
        return solve(0,1)
            
        
