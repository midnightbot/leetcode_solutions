##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        
        queue = [[root,0,0]]
        
        while queue:
            node = queue.pop(0)
            ans.append([node[0].val,node[1],node[2]])
            if node[0].left:
                queue.append([node[0].left,node[1]+1,node[2]-1])
                
            if node[0].right:
                queue.append([node[0].right,node[1]+1,node[2]+1])
                
        ans = sorted(ans, key = lambda x:(x[2],x[1],x[0]))
        result = []
        temp = []
        prevkey = ans[0][2]
        temp.append(ans[0][0])
        print(ans)
        for x in range(1,len(ans)):
            if ans[x][2]!=prevkey:
                result.append(temp)
                temp = [ans[x][0]]
                prevkey = ans[x][2]
                
            else:
                temp.append(ans[x][0])
                
        result.append(temp)
        return result
                
            
            
        
