class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        """
        ## Time Complexity O(26*N)
        ## Space Complexity O(N*26)
        colors = "!" + colors
        neededTime = [float('inf')] + neededTime
        
        n = len(colors)
        
        
        @lru_cache(None)
        def find_ans(indx, prev):
            if indx == n:
                return 0
            
            else:
                ans = float('inf')
                if colors[indx] == prev:
                    ans = min(ans, neededTime[indx] + find_ans(indx+1, prev))        
                else:
                    ans = min(ans, neededTime[indx] + find_ans(indx+1,prev))
                    ans = min(ans, find_ans(indx+1, colors[indx]))
                return ans
            
        return find_ans(1,0)
        """
        
        stack = []
        ans = 0
        
        for x in range(len(colors)):
            #print(stack,ans,x)
            if stack and colors[stack[-1]] == colors[x]:
                
                if neededTime[stack[-1]] > neededTime[x]:
                    ans+=neededTime[x]
                    #stack[-1] = x
                    
                else:
                    ans+=neededTime[stack[-1]]
                    stack[-1] = x
                    
            else:
                stack.append(x)
                
        return ans
        
                
                
                
            
            
        
        
        
