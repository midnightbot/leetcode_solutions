# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        
        #self.explore(root)
        
        #return ans
        queue = [root]
        ans  = []
        
        while queue:
            node = queue.pop()
            if node.left!=None and node.right == None:
                ans.append(node.left.val)
                queue.append(node.left)
            
            elif node.right!=None and node.left == None:
                ans.append(node.right.val)
                queue.append(node.right)
            
            elif node.right!=None and node.left!=None:
                queue.append(node.left)
                queue.append(node.right)
                
                
        return ans
            
        
    def explore(self,root: Optional[TreeNode]):
        ans = []
        
        if root.left!=None and root.right == None:
            ans.append(root.left.val)
            return self.explore(root.left)
            
        elif root.right!=None and root.left == None:
            ans.append(root.right.val)
            return self.explore(root.right)
            
        elif root.right!=None and root.left!=None:
            return self.explore(root.left)
            return self.explore(root.right)
        
        
        return ans

         
        
        
            
        
