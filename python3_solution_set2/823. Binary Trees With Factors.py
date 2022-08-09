##ss
##Solution 1
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mods = 10**9 + 7
        ## no-leaf node is product of leaf nodes
        n = len(arr)
        arr = sorted(arr)
        dp = [1 for x in range(n)]
        indexer = {}
        for x in range(n):
            indexer[arr[x]] = x
        for x in range(n):
            for y in range(x):
                if arr[x]%arr[y] == 0 and (arr[x]//arr[y]) in indexer:
                    k = (arr[x]//arr[y])
                    dp[x]+=dp[y] * dp[indexer[k]]
                    dp[x]%=mods
                        
        return sum(dp)%mods
