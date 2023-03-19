class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:

        ## binary search question

        l = 0
        r = max(buckets)*2

        def find_possible(v):
            ## removed - removed*loss >= poured in

            poured_in = 0
            removed = 0

            for x in buckets:
                if x>=v:
                    removed+=(x-v)
                else:
                    poured_in+=(v-x)

            return removed - (removed*loss/100) >= poured_in

        while r-l>=10**-5:
            mid = (l+r)/2
            if find_possible(mid):
                l = mid

            else:
                r = mid

        return l
