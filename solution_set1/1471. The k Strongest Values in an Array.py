##ss
import heapq
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        
        arr = sorted(arr)
        
        if len(arr)%2==0:
            #median = (arr[len(arr)//2] + arr[len(arr)//2 - 1]) / 2
            median = arr[(len(arr)-1)//2]
            
        else:
            median = arr[len(arr)//2]
            
        ans = []
        i = 0
        j = len(arr) - 1
        print(arr)
        for x in range(k):
            #print(i,j,arr[i],arr[j],median)
            if abs(arr[i] - median) > abs(arr[j] - median):
                ans.append(arr[i])
                i+=1
                
            elif abs(arr[i] - median) < abs(arr[j] - median):
                ans.append(arr[j])
                j-=1
                
            else:
                if arr[i] > arr[j]:
                    ans.append(arr[i])
                    i+=1
                    
                else:
                    ans.append(arr[j])
                    j-=1
        return ans
            
        
