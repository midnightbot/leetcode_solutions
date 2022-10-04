##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        search = [startValue, destValue]
        
        def find(root):
            
            if root is None:
                return None
            
            l = find(root.left)
            r = find(root.right)
            
            if root.val in search:
                return root
            
            if l and r:
                return root
            
            if l and not r:
                return l
            
            else:
                return r
            
            
        node = find(root) ##finding lowest common ancestor
        ##path1 will be "U" * depth of start from node
        
        ##path(start to node) + path(node to dest)
        path1 = self.lpath(node,startValue)
        path2 = self.find_path(node,destValue)
        return path1 + path2
                        
    def find_path(self,node,dest):
        
        q = [[node,""]]
        while q:
            for x in range(len(q)):
                node = q.pop(0)
                
                if node[0].val == dest:
                    return node[1]
                
                if node[0].left:
                    q.append([node[0].left,node[1]+"L"])
                    
                if node[0].right:
                    q.append([node[0].right,node[1]+"R"])
      
    def lpath(self,node,start):
        q = [[node,0]]
        while q:
            for x in range(len(q)):
                node = q.pop(0)
                
                if node[0].val == start:
                    return ''.join("U" for x in range(node[1]))
                
                if node[0].left:
                    q.append([node[0].left,node[1]+1])
                    
                if node[0].right:
                    q.append([node[0].right,node[1]+1])
