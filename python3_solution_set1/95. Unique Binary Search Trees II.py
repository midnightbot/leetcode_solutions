##ss
from itertools import permutations
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        ##brute force, try every combiantion
        ##inserting elements in different order will result in diff trees, so try every insertion order, n! combinations
        ans = []
        seen = set()
        comb = list(list(permutations([x+1 for x in range(n)])))
        for x in range(len(comb)):
            comb[x] = list(comb[x])
        
        #print(comb)
        def insert(val,root):
            #print(val,root)
            if root is None:
                return
            
            elif root.val > val:
                if root.left:
                    insert(val,root.left)
                else:
                    root.left = TreeNode(val,None)
                    return root
                
            else:
                if root.right:
                    insert(val,root.right)
                    
                else:
                    root.right = TreeNode(val,None)
                    return root
         
        def transform(root):
            
            if root is None:
                return "None"
            
            ans = ""
            ans+=str(root.val)
            ans+=";"+transform(root.left)
            ans+=';'+transform(root.right)
            
            return ans
        
        for x in range(len(comb)):
            root = TreeNode(comb[x][0])
            for y in range(1,len(comb[0])):
                #print(comb[x][y])
                insert(comb[x][y],root)
                
                #print(x,root)
            #print(root,ans)
            temp = transform(root)
            if temp not in seen:
            
                ans.append(root)
                seen.add(temp)
            #print(len(ans))
        return ans
            
        
