class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        ## max 'days' subarray such that the sum of max subarray is minimized
        ## looking at the constraints, recursion will not work

        ## working on binary search
        def can_be_done(cap):
            d = 0
            curr = 0
            
            for x in range(len(weights)):
                #print(curr, weights[x])
                if curr + weights[x] <= cap:
                    curr+= weights[x]
                else:
                    d+=1
                    curr = weights[x]
            
            if curr!=0:
                return d+1
            return d


        l = max(weights)
        r = 10**7

        while l < r:
            mid = (l+r)//2

            if can_be_done(mid) <= days:
                r = mid
            else:
                l = mid + 1

        return l
