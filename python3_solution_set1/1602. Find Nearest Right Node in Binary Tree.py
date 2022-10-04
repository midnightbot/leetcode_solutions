##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        
        ##level order traversal
        level = []
        
        queue = [root]
        
        while queue:
            level = []
            prev = -1
            rets = False
            for x in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                prev = node.val
                
                if rets == True:
                    return node
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
                if node == u:
                    rets = True
                    
        return None
                    
        
        
