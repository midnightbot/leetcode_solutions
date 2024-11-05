class Solution:
    def minChanges(self, n: int, k: int) -> int:
        n = str(format(n,'b'))
        k = str(format(k,'b'))

        if len(k) > len(n):
            return -1

        k = "".join(['0' for x in range(len(n)-len(k))]) + k
        ans = 0
        for x in range(len(k)):
            if n[x] == k[x]:
                continue
            elif n[x]=="1" and k[x]=="0":
                ans+=1
            else:
                return -1
        return ans
        
