# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        ans = []
        
        delete = set()
        for x in to_delete:
            delete.add(x)
            
        self.dels(root,delete,ans)
        if root.val not in delete:
            ans.append(root)
        return ans
    
    def dels(self,root,delete,ans):
        
        
        if root is None:
            return None
        
        
        root.left = self.dels(root.left,delete,ans)
        root.right = self.dels(root.right,delete,ans)
        
        
        if root.val in delete:
            if root.left:
                ans.append(root.left)
                
            if root.right:
                ans.append(root.right)
                
                
            return None
            
            
        return root
            
                
        
