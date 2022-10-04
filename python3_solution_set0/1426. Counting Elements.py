##ss
class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        arr = sorted(arr)
        
        ans = 0
        x = 0
        print(arr)
        while x < len(arr):
        
            #print(x)
            print(x,ans)
            count1 = arr.count(arr[x])
            count2 = arr.count(arr[x]+1)
            
            if count1!=0 and count2!=0:
                ans+=count1
            
            x+=count1
            
            
        return ans
