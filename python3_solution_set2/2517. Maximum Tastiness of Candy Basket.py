class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        
        price.sort()

        l = 0
        r = (price[-1] - price[0]) * 2
        n = len(price)
        def find_possible(val):

            i = 0
            prev = -float('inf')
            count = 0
            while i < n and count <k:
                if prev + val <= price[i]:
                    count+=1
                    prev = price[i]
                i+=1

            return count == k

        while l < r:
            mid = (l+r)//2

            if find_possible(mid):
                l = mid + 1

            else:
                r = mid

        return max(l - 1,0)

        
        
