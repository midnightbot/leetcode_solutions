##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        
        def find_nodes(root):
            
            if root:
                if root.left:
                    find_nodes(root.left)
                    
                arr.append(root.val)
                
                if root.right:
                    find_nodes(root.right)

        find_nodes(root)
        #print(arr)
        
        def insert(l,r):
            
            if l > r:
                return None
            
            elif l <= r:
                mid = l + (r-l)//2
                root = TreeNode(arr[mid])
       
                root.left = insert(l,mid-1)
                root.right = insert(mid+1,r) 
                
                return root
                
        return insert(0,len(arr)-1)
        #return root
            
        
        
        
