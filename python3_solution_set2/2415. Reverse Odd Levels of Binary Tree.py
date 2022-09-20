# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        arr = []
        
        q = [root]
        
        while q:
            thislevel = []
            newq = []
            for x in q:
                thislevel.append(x.val)
                
                if x.left:
                    newq.append(x.left)
                    newq.append(x.right)
            arr.append(thislevel)
            q = newq
            
        for x in range(len(arr)):
            if x%2!=0:
                arr[x] = arr[x][::-1]
                
        arrs = []
        for x in arr:
            arrs+=x
        n = len(arrs)
        def make_ans(indx):
            if indx >= n:
                return None
            
            else:
                newroot = TreeNode()
                newroot.val = arrs[indx]
                newroot.left = make_ans(indx*2 + 1)
                newroot.right = make_ans(indx*2 + 2)
                return newroot
   
        return make_ans(0)
                
        
