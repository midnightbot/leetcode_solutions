##ss
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        
        ## as it is a tree
        ## target  will be at 't' dist from vertex1
        ## if more than 't' distance then it cannot reach just jump on it
        
        graph = {x:[] for x in range(1,n+1)}
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        
        def find_path(start,end):
            
            q = [[start,str(start)]]
            visited = set()
            visited.add(start)
            
            while q:
                top,curr_path = q.pop(0)
                if top == end:
                    return curr_path
                
                for nei in graph[top]:
                    if nei not in visited:
                        q.append([nei,curr_path+","+str(nei)])
                        
            
        temp = find_path(1,target)
        comp = temp.split(",")
        #print(temp)
        if len(comp) > t + 1:
            return 0.0
        
        # if len(comp)!=t+1:
        #     diff = t+1-len(comp)
        #     for z in range(diff):
        #         comp.append(comp[-1])
                
        ans = 1
        
        seen = set()
        for x in range(len(comp)-1):
            seen.add(int(comp[x]))
            count = 0
            
            for nei in graph[int(comp[x])]:
                if nei not in seen:
                    count+=1
              
            if count == 0:
                if comp[x] == target: ## at last node and all neis visited, keep jumping on it
                    return ans
                else: 
                    return 0
                
            ans*=1/count
            
        
        if len(comp)!=t+1:
            
            for nei in graph[target]:
                if nei not in seen:## if on last node and can go to some other node, then this target node will be marked visited and we can never get back here again
                    return 0
        return ans
            
        
        
        
        
