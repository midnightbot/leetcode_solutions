##ss
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ##trying to implement it in a heap
        ##heaps in python are min heaps, hence append -ve of number
        ## O(k + nlogk)
        
        
        ans = []
        final_ans = []
        ret_ans = []
        for x in range(min(k,len(nums))):
            heapq.heappush(ans,-1 * nums[x])
         
        maxs = ans[0]
        #maxs = heapq.heappop(ans)
        ret_ans.append(maxs*-1)
        #heapq.heappush(ans,maxs)
        for x in range(1,len(nums)-k+1):
            #ans[x-1] = ans[-1]
            #ans.pop()
            #print(x,ans,nums[x-1])
            ans.remove(-1* nums[x-1])
            heapq.heapify(ans)
            heapq.heappush(ans,-1*nums[x+k-1])
            
            #maxs = heapq.nsmallest(1,ans)
            #print(ans)
            #maxs = heapq.heappop(ans)
            maxs = ans[0]
            ret_ans.append(maxs*-1)
            #heapq.heappush(ans,maxs)
            
        #print(ans)
        #maxs = heapq.heappop(ans)
        #ret_ans.append(maxs)
        return ret_ans
        #print(ans)
        
        
 ## Solution 2
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ans = []
        temp = collections.deque()
        
        l = 0
        r = 0
        ##monotonically dec queue
        ##therefore max element always at the left
        
        while r < len(nums):
            
            while temp and nums[temp[len(temp)-1]] < nums[r]:##pop elements until right head becomes greater than current element
                temp.pop()
                
            temp.append(r)##append the new element
            
            if l > temp[0]:##window changed and if previous window element still in queue remove it
                temp.popleft()
                
            if (r+ 1) >=k:
                ans.append(nums[temp[0]])
                l+=1
                
            r+=1
            
            
        return ans
        
        
