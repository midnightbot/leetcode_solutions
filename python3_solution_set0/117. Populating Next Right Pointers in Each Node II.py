##ss
## Almost same as 116. Populating Next Right Pointers in Each Node 
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        queue = [root]
        if queue[0]==None:
            return root
        c = 0
        while queue:
            c+=1
            queue[len(queue)-1].next = None
            for x in range(len(queue)-2,-1,-1):
                queue[x].next = queue[x+1]
            for x in range(len(queue)):
                node = queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            
        return root
                     
