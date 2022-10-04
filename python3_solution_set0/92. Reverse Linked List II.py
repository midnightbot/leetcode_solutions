# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        temp = []
        temp2 = []
        while head:
            temp.append(head.val)
            head = head.next
            
        #print(temp)
        
        
        for x in range(left-1,right):
            temp2.append(temp[x])
            
        temp2 = temp2[::-1]
        #print(temp2)
        counter = 0
        for x in range(left-1,right):
            temp[x] = temp2[counter]
            counter+=1
            
        #print(temp)
        ans = final = ListNode()
        for x in temp:
            final.next = ListNode(x)
            final = final.next
            
        return ans.next
            
        
