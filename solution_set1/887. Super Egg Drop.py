##ss
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        
        ##'k' eggs, 'n' floors
        
        ## say we are on floor 'x'
        ## if it breaks, we have to check (x-1) down floors with 'k-1' eggs
        ## if it does not break, we have to check (n-x) upper floors with 'k' eggs
        
        def print_dp(dp):
            for x in range(len(dp)):
                print(dp[x])
                
           
        @lru_cache(None)
        def find_ans(n,k):
            if n == 0:
                return 0
                
            elif k == 1:
                return n
                
            else:
                l = 1
                h = n
                
                while l + 1 < h:
                    mid = (l+h)//2
                    
                    breaks = find_ans(mid-1,k-1)
                    not_breaks = find_ans(n-mid,k)
                    
                    if breaks < not_breaks:
                        l = mid
                        
                    elif breaks > not_breaks:
                        h = mid
                        
                    else:
                        l = mid
                        h = mid
                        
                ans = 1 + min(max(find_ans(x-1,k-1), find_ans(n-x,k)) for x in (l,h))
                return ans
            
        return find_ans(n,k)
