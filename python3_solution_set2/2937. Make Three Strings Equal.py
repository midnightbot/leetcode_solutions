class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:

        ## find longest common prefix

        mins = min(len(s1), len(s2), len(s3))
        total = len(s1) + len(s2) + len(s3)

        for x in range(0, mins + 1):
            if s1[:x+1] == s2[:x+1] == s3[:x+1]:
                continue
            else:
                if x!=0:
                    return total - 3*x
                else:
                    return -1
                    

        return 0
        
