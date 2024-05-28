from collections import deque 

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        arr = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        
        ## size of maximum subarry whose sum is less than maxCost
        ans = 0
        q = collections.deque()
        sums = 0
        lens = 0
        for x in range(len(arr)):
            if sums + arr[x] <= maxCost:
                sums+=arr[x]
                q.append(arr[x])
                lens+=1
                ans = max(ans, lens)
            
            else:
                while q and sums+arr[x] > maxCost:
                    temp = q.popleft()
                    sums-=temp
                    lens-=1

                if sums+arr[x] <= maxCost:
                    sums+=arr[x]
                    q.append(arr[x])
                    lens+=1
                    ans = max(ans, lens)
        return ans
