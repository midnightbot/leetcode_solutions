##ss
##write the equations for column valeues, once we get the height of the tree, solve the equation using eval
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        ans = []
        result = []
        q = [[root,0,"(n-1)/2"]]
        ht = 0
        while q:
            for x in range(len(q)):
                node = q.pop(0)
                ht = max(ht,node[1])
                ans.append([node[0].val,node[1],node[2]])
                
                if node[0].left:
                    q.append([node[0].left,node[1]+1,node[2] + "-"+"2**(ht-"+ str(node[1]) +"-"+"1)" ])
                             
                if node[0].right:
                    q.append([node[0].right,node[1]+1,node[2] + "+"+"2**(ht-"+ str(node[1]) +"-"+"1)"])
        n = 2**(ht+1)-1
        #print(n)
        for x in range(len(ans)):
            ans[x][2] = int(eval(ans[x][2]))
            
        #print(ans)
        result = [["" for x in range((2**(ht+1)-1))] for y in range(ht+1)]
        
        for x in range(len(ans)):
            result[ans[x][1]][ans[x][2]] = str(ans[x][0])
            
        return result
