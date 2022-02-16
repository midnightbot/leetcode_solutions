##ss
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        i = 0
        while i < len(arr):
                
            if arr[i]!=target[i]:
                #print("inside")
                if target[i] in arr[i:]:
                    index = arr[i:].index(target[i])
                    arr = arr[:i] + arr[i:i+index+1][::-1] + arr[i+index+1:] 
                    #print(arr)
                else:
                    return False
                    
            i+=1
            
            
        return True
