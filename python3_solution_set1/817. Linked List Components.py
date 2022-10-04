##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        parts = 0
        left = set(nums)
        #print(left)
        
        cons = 0
        while head:
            
            if head.val in left:
                left.remove(head.val)
                cons+=1
                
            elif head.val not in left:
                if cons!=0:
                    parts+=1
                    
                cons = 0
                
            head = head.next
            
        
        return parts + 1 if cons!=0 else parts
            
