class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        ans = []
        checks = []
        temp = -1
        if n==1:
            return 1
        for x in range(len(trust)):
            ans.append(trust[x][1])
            checks.append(trust[x][0])
            
        for y in range(len(ans)):
            count = ans.count(ans[y])
            if count == n-1:
                temp = ans[y]
                break
                
        if temp not in checks:
            return temp
        else:
            return -1
        
