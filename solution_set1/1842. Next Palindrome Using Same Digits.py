##ss
class Solution:
    def nextPalindrome(self, num: str) -> str:
        
        
        def make_num(num): ## just redo this function
            arr = [int(x) for x in num]
            n = len(arr)
            k = n - 2
            while k >= 0:
                if arr[k] < arr[k+1]:
                    break
                k-=1
                
            if k < 0:
                arr = arr[::-1]
                
            else:
                for x in range(n-1, k,-1):
                    if arr[x] > arr[k]:
                        break
                        
                arr[x],arr[k] = arr[k],arr[x]
                arr[k+1:] = arr[k+1:][::-1]
                
            arr = [str(x) for x in arr]
            return "".join(arr)
                    
                    
                
            
        if len(num)%2 == 0:
            half = num[0:len(num)//2]
            if [int(x) for x in half] == sorted([int(x) for x in half], reverse = True):
                return ""
            return make_num(half) + make_num(half)[::-1]
        
        
        else:
            half = num[0:len(num)//2]
            if [int(x) for x in half] == sorted([int(x) for x in half], reverse = True):
                return ""
            return make_num(half) + num[len(num)//2] + make_num(half)[::-1]
            
        ## make next larger number for half
        
        
        
