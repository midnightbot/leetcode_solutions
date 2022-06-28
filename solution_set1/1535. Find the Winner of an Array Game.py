##ss
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        if k>=len(arr):
            return max(arr)
        
        stack = deque()
        cons = 0
        prev_winner = -1
        
        for x in arr:
            stack.append(x)
            
        #print(stack)
        
        
        while cons!=k:
            a = stack.popleft()
            b = stack.popleft()
            #print(a,b)
            if a>b:
                stack.append(b)
                stack.appendleft(a)
                if a == prev_winner:
                    cons+=1
                    
                else:
                    prev_winner = a
                    cons = 1
                    
            else:
                stack.append(a)
                stack.appendleft(b)
                if b == prev_winner:
                    cons+=1
                    
                else:
                    prev_winner = b
                    cons = 1
                    
            #print(prev_winner, stack)
        return prev_winner
