##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        head = list1
        count = 0
        prev = None
        while count !=a:
            count+=1
            prev = list1
            list1 = list1.next
            
        next2 = None
        while count!=b+1:
            count+=1
            next2 = list1
            list1 = list1.next
        
        #next2.next = None
        prev.next = list2
        
        while list2.next!=None:
            list2 = list2.next
            
        list2.next = next2.next
        next2.next = None
        #print(prev,next2,head)
        return head   
        
