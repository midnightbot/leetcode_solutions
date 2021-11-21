# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        n = len(inorder)
        
        if n == 0:
            return None
        
        return self.buildtree(inorder,postorder,0,n,0,n)
        
        
    def buildtree(self,inorder,postorder,i1,i2,j1,j2):
        #print(i1)
        if i1>=i2 or j1>=j2:
            return None
        root = TreeNode(postorder[j2-1])
        index = inorder.index(postorder[j2-1])
        diff = index - i1
        root.left = self.buildtree(inorder,postorder,i1,i1+diff,j1,j1+diff)
        root.right = self.buildtree(inorder,postorder,i1+diff+1,i2,j1+diff,j2-1)
        
        return root
        
        
        
