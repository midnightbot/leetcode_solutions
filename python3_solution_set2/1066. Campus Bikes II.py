class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        def find_dist(x,y):
            return abs(x[0]-y[0]) + abs(x[1] - y[1])

        memo = {}
        def find_ans(p, arr):
            if p < 0:
                return 0
            elif (p,tuple(arr)) in memo:
                return memo[(p, tuple(arr))]

            else:
                ans = float('inf')

                for i in range(len(arr)):
                    if arr[i] == 0:
                        arr[i] = 1
                        ans = min(ans, find_dist(bikes[i], workers[p]) + find_ans(p-1, arr))
                        arr[i] = 0

                memo[p, tuple(arr)] = ans

                return ans

        return find_ans(len(workers)-1, [0 for x in range(len(bikes))])
