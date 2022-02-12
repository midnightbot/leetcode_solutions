##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.pointer = -1
        self.inorder(root)
        #print(self.arr)
    def inorder(self,root):
        if root is None:
            return 
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
        
        
        

    def next(self) -> int:
        self.pointer+=1
        return self.arr[self.pointer]
        

    def hasNext(self) -> bool:
        return self.pointer + 1 < len(self.arr)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
