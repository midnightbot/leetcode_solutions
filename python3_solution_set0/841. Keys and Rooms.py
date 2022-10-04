##ss
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        ans = set()
        visited = []
        queue = [0]
        
        while len(queue)!=0:
            #print(queue)
            node = queue.pop(0)
            
            if node not in visited:
                visited.append(node)
                #print(rooms[node])
                for y in range(len(rooms[node])):
                    queue.append(rooms[node][y])
                    
        return len(visited) == len(rooms)
        
