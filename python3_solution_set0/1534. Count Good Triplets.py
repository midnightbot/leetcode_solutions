class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for x in range(len(arr)):
            for y in range(x+1,len(arr)):
                for z in range(y+1,len(arr)):
                    if(abs(arr[x]-arr[y])<=a and abs(arr[y]-arr[z])<=b and abs(arr[x]-arr[z])<=c):
                        #print(str(arr[x])+""+str(arr[y])+""+str(arr[z]))
                        count+=1
                        
        return count
