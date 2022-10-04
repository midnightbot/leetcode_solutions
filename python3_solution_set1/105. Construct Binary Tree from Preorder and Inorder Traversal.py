# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        ##preorder -> root.val root.left  root.right
        ##inorder -> root.left root.val  root.right
        
        def make_tree(preorder,inorder):
            #print(preorder,inorder)
            if len(preorder) == 0 or len(inorder) == 0:
                return None
            
            newnode = TreeNode(preorder[0])
            
            indx = inorder.index(newnode.val)
            
            newnode.left = make_tree(preorder[1:indx+1],inorder[0:indx])
            newnode.right = make_tree(preorder[indx+1:],inorder[indx+1:])
            
            return newnode
                
        return make_tree(preorder,inorder)
            
        
