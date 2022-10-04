##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        temp = []
        
        temps = head
        
        while head!=None:
            temp.append(head.val)
            head = head.next
            
        i = 0
        j = len(temp) - 1
        
        ans = []
        
        while i <= j:
            if i!=j:
                ans.append(temp[i])
                ans.append(temp[j])
                
            else:
                ans.append(temp[i])
            i+=1
            j-=1
        
        c = 0
        anss = temps
        
        while temps!=None:
            temps.val = ans[c]
            c+=1
            temps = temps.next
            
        return anss
        
