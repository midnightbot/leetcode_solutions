##ss
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        #print(node.val,self.visited)
        
        if not node:
            return node
        
        elif node not in self.visited:
            root = Node(node.val,[])
            #root.val = node.val
            #visited.add(node.val)
            self.visited[node] = root
            if  node.neighbors:
                root.neighbors = [self.cloneGraph(x) for x in node.neighbors] 
                
            
            return self.visited[node]
        
        elif node in self.visited:
            return self.visited[node]
            
        
