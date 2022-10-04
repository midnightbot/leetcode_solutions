##ss
## Simple BFS/DFS
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        queue = [start]
        
        while queue:
            node = queue.pop(0)
            
            #print(node)
            if arr[node] == 0:
                return True
                queue = []
            
            elif arr[node] > 0:
                if node+arr[node] < len(arr):
                    queue.append(node+arr[node])
                    
                if node - arr[node] >=0:
                    queue.append(node - arr[node])
            arr[node] = -1     
                    
        return False
        
