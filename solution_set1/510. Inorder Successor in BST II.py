##ss
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        
        #print(node.val)
        ## answer will be min(parentval,node.right.val) is node is left child of its parent
        ## answer will be node.right.val if node is right child of its parent

        if node.parent is None:
            if node.right is None:
                return None
            
            else:
                temp = node.right
                while temp.left:
                    temp = temp.left
                    
                return temp
            
        parentval = node.parent.val
        nodeval = node.val
        print(nodeval,parentval)
        if node.right:
            node = node.right
            while node.left:
                node = node.left
                
            return node
            
        else:## right child
            while node.parent and node == node.parent.right:
                node = node.parent
                
            return node.parent
