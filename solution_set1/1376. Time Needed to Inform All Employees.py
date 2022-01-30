##ss
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        time = 0
        children = {}
        visited = set()
        queue = []
        for x in range(len(manager)):
            if manager[x] not in children:
                children[manager[x]] = [x]
                
            else:
                children[manager[x]].append(x)
                
        #print(children)
        queue.append((headID,0))
        
        while queue:
            for x in range(len(queue)):
                node = queue.pop(0)
                if node[0] in children:
                    for z in children[node[0]]:
                        thistime = node[1] + informTime[node[0]]
                        time = max(time,thistime)
                        queue.append((z,thistime))
                        
                        
        return time
        
