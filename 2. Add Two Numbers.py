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
        
        temp1 = temp1[::-1]
        temp2 = temp2[::-1]
        #print(temp1)
        s1 = [str(i) for i in temp1] ##converting list of integers to integer
        res1 = int("".join(s1))
        
        s2 = [str(i) for i in temp2]
        res2 = int("".join(s2))
        
        ans = res1 + res2
        final = [int(x) for x in str(ans)] ## converting int answer back to list
        final = final[::-1]
        
        finals = temp = ListNode()
        for x in final:
            temp.next = ListNode(x)
            temp = temp.next
            
        return finals.next
        
        
