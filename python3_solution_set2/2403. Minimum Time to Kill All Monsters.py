import math
class Solution:
    def minimumTime(self, power: List[int]) -> int:
        
        ## gain = 1 (initially) 
        
        ## gain+=1 (killing a monster)
        
        
        n = len(power)
        @lru_cache(None)
        def find_ans(killed, gains):
            if killed == 2**n-1:
                return 0

            else:
                ans = float('inf')
                for x in range(n):
                    temps = 1 << x
                    if (killed & temps) == 0:
                        ans = min(ans , math.ceil(power[x]/gains) + find_ans(killed | temps, gains+1))
                return ans

        return find_ans(0, 1)
        
