import heapq
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        @cache
        def find_ans(r, c):
            return r*(c+1)*(c+1)
        ## all mechanics can work simultaneously
        ## distirbute cars to mechanics and return max of the time of all mechanics
        ## try to minimize this max time

        ## r*n*n time taken for n cars

        ## for every car take the mechanic whose time will be less than all other mechanics
        temp = Counter(ranks)
        q = []
        for x in temp:
            ## [total cost, curr_cars, rank, counter of such mechanics] if one car is added to this mechanic
            heapq.heappush(q, [x, 0, x, temp[x]])
        while cars > 0:
            curr_time, curr_cars, rank, cnt = heapq.heappop(q)
            cars-=cnt
            curr_cars+=1
            heapq.heappush(q, [find_ans(rank, curr_cars), curr_cars, rank, cnt])

        return curr_time
