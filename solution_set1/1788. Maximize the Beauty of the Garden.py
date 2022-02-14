##ss
class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        
        ans = -float('inf')
        full = [0 for x in range(len(flowers))] ##prefix sum of the whole array
        neg = [0 for x in range(len(flowers))] ##prefix sum of negatives of the array
        
        full[0] = flowers[0]
        for x in range(1,len(flowers)):
            full[x] = (full[x-1] + flowers[x])
            
        if flowers[0] < 0:
            neg[0] = flowers[0]
            
        for x in range(1,len(flowers)):
            if flowers[x] < 0:
                neg[x] = neg[x-1] + flowers[x]
                
            else:
                neg[x] = neg[x-1]
         
        full.insert(0,0)
        neg.insert(0,0)
        #print(full,neg)
    
        index = {}  ##contains first and last occurence index of any element
        ##so basically we have to check for all these valid gardens
        ##to maximize beauty, remove negative plants if any between these two plants
        
        
        
        for x in range(len(flowers)):
            if flowers[x] in index:
                index[flowers[x]][1] = x
                
            else:
                index[flowers[x]] = [x,x]
        
        
        for z in index:
            if index[z][1] - index[z][0] >= 1 and z>=0: ##if the number considered at ends is positive, we can simply remove all negative flowers from between as the size of the remaining will always be greater than or equal to 2
                
                ans = max(ans,(full[index[z][1]+1] - full[index[z][0]]) - (neg[index[z][1]+1] - neg[index[z][0]]))
                
                
            elif index[z][1] - index[z][0] >=1 and z<0:##if the number considered at ends is negative, we cannot remove all the elements from this grp as it will be invalid garden
                ##hence in this case there are 2 possibilities
                ##case1 : if all numbers between the two ends are negative, then remove all of them and answer will be 2*(boundary value)
                
                ##case2: there are some postive integers in between, then remove only negative numbers, say i,j is the boundary range, we have to find the max positive value we can get in range i+1 ...j-1 by removing all the negative plants
                ans = max(ans, 2*z, 2*z + (full[index[z][1]] - full[index[z][0]+1]) - (neg[index[z][1]] - neg[index[z][0]+1]))
                
        return ans
                
                
        
        
        return ans
