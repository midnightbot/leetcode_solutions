import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        

        if n==1:
            return 1

        final = set()
        available = []
        heapq.heappush(available, 1)
        count = 0

        while count!=n:
            top = heapq.heappop(available)
            if top not in final:
                count+=1
                final.add(top)

                for it in primes:
                    new_num = top*it
                    heapq.heappush(available, new_num)
                    #available.add(new_num)

        #print(final)
        return max(final)



