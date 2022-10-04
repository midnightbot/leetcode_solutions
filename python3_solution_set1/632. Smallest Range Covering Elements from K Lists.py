##ss
##Solution 1(TLE)
#from container import SortedList
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        ## easy O(n^2) answer
        
        combine = []
        size = float('inf')
        ans = []
        alls = len(nums)
        for x in range(len(nums)):
            for y in range(len(nums[x])):
                combine.append([nums[x][y],x])
                
        combine = sorted(combine, key = lambda x:x[0])
        #print(combine)
        seen = set()
        
        for x in range(len(combine)):
            seen = set()
            for y in range(x,len(combine)):
                seen.add(combine[y][1])
                
                if len(seen) == alls:
                    #print(seen,x,y,size,combine[x][0],combine[y][0])
                    #seen = set()
                    thisrange = combine[y][0]- combine[x][0]
                    if thisrange < size:
                        size = thisrange
                        ans = [combine[x][0], combine[y][0]]
                        
                    elif thisrange == size:
                        if combine[x][0] < ans[0]:
                            ans = [combine[x][0], combine[y][0]]
                            
                    break
                            
        
        return ans
        
        
##Solution 2(Accepted)
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        q = [(nums[x][0],x,0) for x in range(len(nums))]
        
        heapq.heapify(q)
        
        end = max(nums[x][0] for x in range(len(nums)))

        ans = [-10**10, 10**10]
        while q:
            l , grp , indx = heapq.heappop(q)
            
            if end - l < ans[1] - ans[0]:
                ans = [l,end]
                
                
            if indx == len(nums[grp]) - 1:
                return ans
            
            end = max(end, nums[grp][indx+1])
            
            heapq.heappush(q, (nums[grp][indx+1], grp, indx+1))
