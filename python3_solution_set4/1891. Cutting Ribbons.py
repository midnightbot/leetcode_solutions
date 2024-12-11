class Solution:
    def is_possible(self, val):
        cnt = 0
        for x in self.ribbons:
            cnt+=x//val
    
        return cnt

    def maxLength(self, ribbons: List[int], k: int) -> int:
        ## ss
        ## simple binary search
        ## for each `val` find if it can be a possible ans, if not adjust accordingly
        self.ribbons = sorted(ribbons, reverse = True)
        self.k = k
        l = 1
        r = max(ribbons) + 1
        result = 0
        # print("here", self.is_possible(5))
        while l <= r:
            mid = (l+r+1)//2
            # print(mid)
            ans = self.is_possible(mid)
            # print(mid, ans)
            if ans == self.k:
                result = max(result, mid)
                l = mid + 1
            
            elif ans > self.k:
                result = max(result, mid)
                l = mid + 1

            else:
                r = mid - 1
        return result

            
        
