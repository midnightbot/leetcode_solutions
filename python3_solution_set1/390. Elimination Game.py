##ss
##Solution 1 (Time Limit Exceeded 3375/ 3377 test cases passed)
class Solution:
    def lastRemaining(self, n: int) -> int:
        
        arr = [x for x in range(1,n+1)]
        
        #print(arr)
        ans = {'ans' : -1}
        def find_winner(arr, op):
            
            if len(arr) == 1:
                ans['ans'] = arr[0]
            
            else:
                if op == 0:
                    new_arr = []
                    for x in range(1,len(arr),2):
                        new_arr.append(arr[x])
                        
                    find_winner(new_arr,1)
                    
                else:
                    new_arr = []
                    arr = arr[::-1]
                    for x in range(1,len(arr),2):
                        new_arr.append(arr[x])
                        
                    find_winner(new_arr[::-1],0)
                    
        k = find_winner(arr,0)
        return ans['ans']
        
        
  ##Solution 2 (Accepted)
  class Solution:
    def lastRemaining(self, n: int) -> int:
        
        #[,2,,,,6,,,]
        #arr = [x for x in range(1,n+1)]
        
        #print(arr)
        
        op = True
        left = n
        jump = 1
        start = 1
        
        while left > 1:
            
            if op or left%2==1:
                start+=jump
                
            left = left // 2
            jump*=2
            op = not op
            #print(left, jump, start)
            
        return start
            
            
