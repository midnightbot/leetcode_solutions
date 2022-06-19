class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        
        
        if str(num)[-1] == str(k):
            return 1
        
        opts = set()
        
        for x in range(3000):
            if str(x)[-1] == str(k):
                opts.add(x)
            
            if x > num:
                break
                
        ans = float('inf')
        if 0 in opts:
            opts.remove(0)
            
        if num in opts:
            return 1
        
        if len(opts) == 0:
            return -1
        
        if len(opts) == 1:
            if num%list(opts)[0] == 0:
                return num//list(opts)[0]
            else:
                return -1
        @lru_cache(None)
        def make_ans(left):
            if left < 0:
                return float('inf')
            
            if left == 0:
                return 0
            elif left in opts:
                return 1
            
            else:
                ans = float('inf')
                for x in opts:
                    ans = min(ans, 1 + make_ans(left-x))
                    
                return ans
            
        res = make_ans(num)
        return res if res!=float('inf') else -1
        
