class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:

        arr = [[aliceValues[x] + bobValues[x],x] for x in range(len(aliceValues))]
        arr = sorted(arr, reverse=True, key = lambda x:x[0])
        
        l = 0
        r = 0
        for x in range(len(arr)):
            if x%2==0:
                l+=aliceValues[arr[x][1]]
            else:
                r+=bobValues[arr[x][1]]

        if l > r:
            return 1
        elif l < r:
            return -1
        return 0
