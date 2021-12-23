##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        ans = []
        self.expand(root,0,ans,0)
        #print(ans)
        ans = sorted(ans,key = lambda x:(x[1],x[2]))
        
        col_ans = []
        temp = [ans[0][0]]
        for x in range(1,len(ans)):
            if ans[x][1] == ans[x-1][1]:
                temp.append(ans[x][0])
                
            else:
                col_ans.append(temp)
                temp = []
                temp.append(ans[x][0])
                
        col_ans.append(temp)
        return col_ans
            
        
    
    
    def expand(self,root,col,ans,height):
        
        if root!=None:
            ans.append([root.val,col,height])
            
            self.expand(root.left,col-1,ans,height+1)
            self.expand(root.right,col+1,ans,height+1)
            
 

                
                
        
