class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        ## either a request is valid or not valid
        ## try all possible combinations to see the ans
        l = len(requests)

        for x in range(l, 0 , -1):
            for y in combinations(requests, x):
                if Counter(a for a,b in y) == Counter(b for a,b in y):
                    return x

        return 0

