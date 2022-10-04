##ss
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        q = ["0000"]
        
        d = set(deadends)
        cost = 0
        visited = set()
        visited.add('0000')
        while q:
            for x in range(len(q)):
                node = q.pop(0)
                
                if node == target:
                    return cost
                
                elif node in d:
                    continue
                    
                else:
                    for y in range(4):
                        indx = int(node[y])
                        
                        nei1 = node[:y] + str((indx + 1)%10) + node[y+1:]
                        nei2 = node[:y] + str((indx - 1) % 10) + node[y+1:]
                        
                        for nei in [nei1,nei2]:
                            if nei not in visited:
                                visited.add(nei)
                                q.append(nei)
                                
            cost+=1
            
        return -1
        
