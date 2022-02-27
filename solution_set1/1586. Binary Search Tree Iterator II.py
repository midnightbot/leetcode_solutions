##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.a = self.inorder(root)
        self.ptr = -1
        
        
        
    def inorder(self,root):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []
    def hasNext(self) -> bool:
        return self.ptr < len(self.a) - 1
        

    def next(self) -> int:
        self.ptr+=1
        return self.a[self.ptr]

    def hasPrev(self) -> bool:
        return self.ptr > 0
    
        

    def prev(self) -> int:
        self.ptr-=1
        return self.a[self.ptr]
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()
