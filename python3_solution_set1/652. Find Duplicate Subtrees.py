##ss
##Solution1 (Time Limit Exceeded)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        def expand(node1,node2):
            
            if node1 is None and node2 is None:
                return True
            
            elif node1 is None and node2 is not None:
                return False
            
            elif node2 is None and node1 is not None:
                return False
            
            else:
                return node1.val == node2.val and expand(node1.left,node2.left) and expand(node1.right,node2.right)
            
            
        ans  = set()
        buckets = {}
        #visited = set()
        
        q = [root]
        
        while q:
            for x in range(len(q)):
                node = q.pop(0)
                varss = False
                if node.val in buckets:
                    for z in buckets[node.val]:
                        #print("inside")
                        if expand(node,z):
                            ans.add(z)
                            varss = True
                            break
                            
                    if varss == False:
                        buckets[node.val].append(node)
                        
                else:
                    buckets[node.val] = [node]
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
        #print(buckets)
        return ans
                        
                        
##Solution2 (Accepted)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        seen = set()
        
        dicts = {}
        def expansion(root):
            if root is None:
                return "Null"
            
            else:
                ans = str(root.val)
                
                ans+="," + expansion(root.left)
                ans+=","+expansion(root.right)
                
            dicts[ans] = dicts.get(ans,0) + 1
            
            if dicts[ans] == 2:
                seen.add(root)
            return ans  
        expansion(root)
        return seen
        
        
        

                    
