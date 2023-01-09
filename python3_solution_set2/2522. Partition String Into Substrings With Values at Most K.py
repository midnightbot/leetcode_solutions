class Solution:
    def minimumPartition(self, s: str, k: int) -> int:

        n = len(s)
        if max([int(x) for x in s]) > k:
            return -1

        i = 0
        curr = ""
        count = 0
        while i < n:
            #print(i, s, s[i])
            if int(curr + s[i]) <= k:
                curr+=s[i]
                i+=1
            else:
                curr = s[i]
                count+=1
                i+=1
                
        if curr!="":
            count+=1
        return count

                


