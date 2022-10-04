##ss
##Solution 1 (Time Limit Exceeded)
import copy
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        ##set1 and set2
        
        ##elem either in set1 or set2
        ans = []
        p1 = []
        p2 = []
        self.dp(nums,p1,p2,ans)
        if len(ans) >0:
            return True
        else:
            return False
        
    def dp(self,arr,p1,p2,ans):
        #print(p1,p2,ans)
        if len(arr) == 0:
            if sum(p1) == sum(p2):
                #print("inside")
                ans.append(1)
                
                
        else:
            for x in range(len(arr)):
                temp = arr.copy()
                temp.pop(x)
                newp1 = p1.copy()
                newp2 = p2.copy()
                newp1.append(arr[x])
                newp2.append(arr[x])
                self.dp(temp,newp1,p2,ans)
                self.dp(temp,p1,newp2,ans)
                
 ##Solution 2
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        @lru_cache(None)
        def dp(nums,i,sums):
            if sums == 0:
                return True
            if i == len(nums)-1 or sums < 0:
                return False
            
            else:
                ans = (dp(nums,i+1,sums-nums[i]) or dp(nums,i+1,sums))
                return ans
            
            
        check = sum(nums)
        if check%2!=0:
            return False
        
        return dp(tuple(nums),0,check//2)
        
        
