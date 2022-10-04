##ss
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ##greedy approach
        ##similar to triathalon question learned in greedy lecture
        ##suppose each task involves 2 parts parta and partb
        ##parta to be done before partb
        ##order in which tasks are done will be sorted acctording to tasks that require more time to complete partb
        ##link : https://github.com/midnightbot/CSCI-570/blob/main/content/week3/Lecture%20Notes%20-%203.pdf
        comp = []
        for x in range(len(plantTime)):
            comp.append([plantTime[x],growTime[x]])
            
        comp = sorted(comp,key = lambda x:(-x[1],x[0]))
        
        result = -1
        starttime = 0
        for x in range(len(comp)):
            result = max(result,starttime + comp[x][0]+comp[x][1])
            starttime+=comp[x][0]
            
        return result
        
