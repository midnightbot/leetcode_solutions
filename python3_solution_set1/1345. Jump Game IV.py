##ss
##simple bfs
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        #edges = {}
        
        freq = {}
        for x in range(len(arr)):
            if arr[x] in freq:
                freq[arr[x]].append(x)
                
            else:
                freq[arr[x]] = [x]


        
        steps = 0
        #print(freq)
        queue = [0]
        visited = set()
        #freq.clear()
        while queue:
            
            for x in range(len(queue)):
                node = queue.pop(0)
                visited.add(node)
                
                if node == len(arr)-1:
                    return steps
                
                for adj in freq[arr[node]]:
                    if adj not in visited:
                        queue.append(adj)
                        visited.add(adj)
                 
                freq[arr[node]].clear()
                for adj in [node+1,node-1]:
                    if 0 <=adj < len(arr) and adj not in visited:
                        visited.add(adj)
                        queue.append(adj)
                        
            steps+=1
                        
                
            
