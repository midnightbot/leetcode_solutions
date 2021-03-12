class Solution:
    def trimMean(self, arr: List[int]) -> float:
        
        arr = sorted(arr)
        length = len(arr)
        temp = int(length*0.05)
        sums=0
        #print(" "+str(temp))
        for x in range(temp,length-temp,1):
            #print(sums)
            sums+=arr[x]
            
        
        return (sums/(length-temp*2))
        
