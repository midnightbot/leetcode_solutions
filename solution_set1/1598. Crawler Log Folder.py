##ss
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        steps = 0
        
        for x in range(len(logs)):
            if logs[x] =="../":
                steps-=1
                steps = max(steps,0)
                
            elif logs[x] == './':
                continue
                
            else:
                steps+=1
                
        return steps
        
