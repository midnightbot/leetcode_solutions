##ss
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        ans = [0 for x in range(num_people)]
        
        start = 1
        
        i = 0
        
        while candies >= start:
            ans[i]+=start
            candies-=start
            start+=1
            i+=1
            i = i % num_people
            #print(ans)
        ans[i]+=candies
        
        return ans
        
