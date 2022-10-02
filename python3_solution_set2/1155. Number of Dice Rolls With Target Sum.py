class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        mods = 10**9 + 7
        @cache
        def find_ans(count, sums):
            #print(count, sums)
            if sums == 0 and count == 0:
                return 1
            
            elif (sums < 0 and count!=0) or (count < 0 and sums > 0):
                return 0
            
            else:
                ans = 0
                for x in range(1,k+1):
                    ans+=find_ans(count-1, sums-x)
                    ans%=mods
                return ans%mods
            
        return find_ans(n,target)%mods
                
                
        
