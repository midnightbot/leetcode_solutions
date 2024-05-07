# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        while head:
            arr.append(int(head.val))
            head = head.next

        carry=0
        for x in range(len(arr)-1,-1,-1):
            arr[x]*=2
            arr[x]+=carry
            if arr[x] >= 10:
                carry = arr[x]//10
                arr[x]%=10
            else:
                carry = 0
        if carry!=0:
            arr = [carry] + arr
        n = len(arr)
        def make_ll(indx):
            if indx == n:
                return None
            else:
                new_node = ListNode()
                new_node.val = arr[indx]
                new_node.next = make_ll(indx+1)
                return new_node

        return make_ll(0)

        
