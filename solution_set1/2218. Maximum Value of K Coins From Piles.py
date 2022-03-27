##ss
##Solution1 (TLE)
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        ##take 'k' coins
        ## for each pile take some number of coins such that total coins = k
        
        
        @lru_cache(None)
        def find_max(seen,k):
            if k == 0:
                vis = seen.split(",")
                vis = [int(x) for x in vis]
                res = 0
                for x in range(len(piles)):
                    res+=sum(piles[x][0:vis[x]])
                    
                return res
            
            else:
                vis = seen.split(",")
                vis = [int(x) for x in vis]
                ans = -1
                for z in range(len(piles)):
                    if vis[z] < len(piles[z]):
                        vis[z]+=1
                        vis = [str(x) for x in vis]
                        ans = max(ans, find_max(",".join(vis),k-1))
                        vis = [int(x) for x in vis]
                        
                        vis[z]-=1
                        
                return ans
            
        return find_max(",".join(["0" for x in range(len(piles))]), k)
        
        
## SOlution 2 (Accepted)
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        ##take 'k' coins
        ## for each pile take some number of coins such that total coins = k
        
        prefix_sum = copy.deepcopy(piles)
        for x in range(len(prefix_sum)):
            for y in range(1,len(prefix_sum[x])):
                prefix_sum[x][y]+=prefix_sum[x][y-1]
                
        #print(prefix_sum)
        
        @lru_cache(None)
        def find_max(pos,k):
            
            if k == 0:
                return 0
            
            elif pos == len(piles) and k!=0:
                return -float('inf')
            
            else:
                ans = find_max(pos+1,k) ##no coin selected from this pile
                
                for z in range(min(len(piles[pos]), k)): ## 1 -to- min(len(pile[pos]),k) coins selected
                    ans = max(ans, prefix_sum[pos][z] + find_max(pos+1,k-z-1))
                    
                return ans
            
        return find_max(0,k)
