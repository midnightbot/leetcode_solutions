# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp1 = []
        temp2 = []
        
        while l1:
            temp1.append(l1.val)
            l1 = l1.next
            
        while l2:
            temp2.append(l2.val)
            l2 = l2.next
            
        var1 = [str(i) for i in temp1]
        res1 = int("".join(var1))
        
        var2 = [str(i) for i in temp2]
        res2 = int("".join(var2))
        
        nums = res1 + res2
        count = [int(x) for x in str(nums)]
        
        final = ans = ListNode()
        for x in count:
            ans.next = ListNode(x)
            ans = ans.next
            
        return final.next
        
