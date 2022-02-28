##ss
##Solution1 (Time Complexity O(n))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        
        ##python heaps are min heaps
        
        ans = []
        q = [root]
        
        while q:
            for x in range(len(q)):
                node = q.pop(0)
                
                if len(ans) < k:
                    heapq.heappush(ans , (-1 * abs(node.val - target),node.val))
                    
                elif len(ans) == k:
                    top = heapq.heappop(ans)
                    if top[0] * -1 > abs(node.val - target):
                        heapq.heappush(ans, (-1 * abs(node.val - target), node.val))
                    else:
                        heapq.heappush(ans,top)
                        
                        
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
        for x in range(len(ans)):
            ans[x] = ans[x][1]
            
        return ans
        
        
