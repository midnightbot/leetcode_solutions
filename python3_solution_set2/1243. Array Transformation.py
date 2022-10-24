class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        
        
        done = True
        n = len(arr)
        while done:
            op = 0
            new_arr = []
            for x in range(1,n-1):
                if arr[x-1] > arr[x] and arr[x+1] > arr[x]:
                    op+=1
                    new_arr.append(arr[x]+1)
                    
                elif arr[x-1] < arr[x] and arr[x+1] < arr[x]:
                    op+=1
                    new_arr.append(arr[x]-1)
                else:
                    new_arr.append(arr[x])
            
            arr = [arr[0]] + new_arr + [arr[-1]]
            if op == 0:
                done = False
                
        return arr
