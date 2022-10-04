##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        
        self.root = root
        

    def insert(self, val: int) -> int:
        
        ptr = self.root
        
        q = [ptr]
        
        while q:
            top = q.pop(0)
            if top.left:
                q.append(top.left)
                
            else:
                top.left = TreeNode(val)
                return top.val
                break
                
            if top.right:
                q.append(top.right)
                
            else:
                top.right = TreeNode(val)
                return top.val
                break
                
        

    def get_root(self) -> Optional[TreeNode]:
        
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
