##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        comp = []
        
        while head:
            comp.append(head.val)
            head = head.next
            
        ans = [-1, -1]
        if len(comp) <=2:
            return ans
        
        crpoints = []
        
        for x in range(1,len(comp) - 1):
            if comp[x-1] < comp[x] and comp[x] > comp[x+1]:
                crpoints.append(x)
            
            elif comp[x-1] > comp[x] and comp[x] < comp[x+1]:
                crpoints.append(x)
                
        if len(crpoints) < 2:
            return [-1,-1]
        
        mins = float('inf')
        
        for x in range(1,len(crpoints)):
            mins = min(mins, crpoints[x] - crpoints[x-1])
            
        return [mins, crpoints[-1] - crpoints[0]]
