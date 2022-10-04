##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        ans = [[-1 for x in range(n)] for y in range(m)]
        
        arr = []
        while head!=None:
            arr.append(head.val)
            head = head.next
            
        diff = m*n - len(arr)
        
        for x in range(diff):
            arr.append(-1)
            
        indx = 0
        startrow = 0
        endrow = m - 1
        startcol = 0
        endcol = n-1
        
        if m*n == 1:
            return [[arr[0]]]
        while startrow < endrow and startcol < endcol:
            
            for x in range(startcol,endcol+1):
                ans[startrow][x] = arr[indx]
                indx+=1
                
            #print(indx)
            for x in range(startrow+1,endrow+1):
                ans[x][endcol] = arr[indx]
                indx+=1
                
            #print(indx)
            for x in range(endcol-1,startcol-1,-1):
                ans[endrow][x] = arr[indx]
                indx+=1
                
            #print(indx)
            for x in range(endrow-1,startrow,-1):
                #print(x,indx)
                ans[x][startcol] = arr[indx]
                indx+=1
                
            #print(ans)
            startrow+=1
            endrow-=1
            startcol+=1
            endcol-=1
        
        if startrow==endrow and startcol!=endcol:
            for x in range(startcol,endcol+1):
                ans[startrow][x] = arr[indx]
                indx+=1
                
        if startcol==endcol and startrow!=endrow:
            for x in range(startrow,endrow+1):
                ans[x][startcol] = arr[indx]
                indx+=1
            
        #print(startrow,endrow,startcol,endcol)
        
        return ans
