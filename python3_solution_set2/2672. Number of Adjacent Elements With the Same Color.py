class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:

        ## adjacent element nums[j] == nums[j+1]
        ## simple solution
        ## every time we color something, just see its two neighbours and see if any pair was destoryed or if any new pair was made
        ## uncolored adjacent elements are not counted
        arr = [0 for x in range(n)]
        ans = []
        count = 0

        for x,y in queries:
            tmp = 0
            if x+1<n and arr[x] == arr[x+1] and arr[x]!=0:
                tmp-=1
            if x-1>=0 and arr[x] == arr[x-1] and arr[x]!=0:
                tmp-=1

            arr[x] = y
            if x+1<n and arr[x] == arr[x+1]:
                tmp+=1
            if x-1>=0 and arr[x] == arr[x-1]:
                tmp+=1
            
            count+=tmp
            count = max(count,0)
            
            ans.append(count)


        return ans
