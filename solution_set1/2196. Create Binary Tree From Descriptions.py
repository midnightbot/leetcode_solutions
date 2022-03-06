##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        seen = {}
        indeg = {}
        def create_tree(desc):
            
            p1 = desc[0]
            p2 = desc[1]
            indeg[p2] = indeg.get(p2,0) + 1
            indeg[p1] = indeg.get(p1,0)
            if p1 in seen:
                if desc[2] == 1:
                    if p2 in seen:
                        seen[p1].left = seen[p2]
                        
                    else:
                        p2node = TreeNode(p2)
                        seen[p1].left = p2node
                        seen[p2] = p2node
                else:
                    if p2 in seen:
                        seen[p1].right = seen[p2]
                
                    else:
                        p2node = TreeNode(p2)
                        seen[p1].right = p2node
                        seen[p2] = p2node
                        
            else:
                if desc[2] == 1:
                    p1node = TreeNode(p1)
                    seen[p1] = p1node
                    if p2 in seen:
                        seen[p1].left = seen[p2]
                        
                    else:
                        p2node = TreeNode(p2)
                        seen[p1].left = p2node
                        seen[p2] = p2node
                        
                else:
                    p1node = TreeNode(p1)
                    seen[p1] = p1node
                    if p2 in seen:
                        seen[p1].right = seen[p2]
                
                    else:
                        p2node = TreeNode(p2)
                        seen[p1].right = p2node
                        seen[p2] = p2node
            
            
            
        for x in range(len(descriptions)):
            create_tree(descriptions[x])
           
        #print(indeg)
        for x in indeg:
            if indeg[x] == 0:
                return seen[x]
        
