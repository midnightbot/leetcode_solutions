##ss
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        ans = []
        
        for x in range(len(ops)):
            if ops[x] == "+":
                ans.append(ans[len(ans)-1]+ans[len(ans)-2])
                
            elif ops[x] == "C":
                ans.pop(len(ans)-1)
                
            elif ops[x] == "D":
                ans.append(2*ans[len(ans)-1])
                
            else:
                ans.append(int(ops[x]))
                
                
        return sum(ans)
        
