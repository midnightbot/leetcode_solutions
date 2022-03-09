##ss
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        ##select atmost 2 people
        ## w1 + w2 <= limit
        
        ans = 0
        people = sorted(people)
        
        i = 0
        j = len(people) - 1
        
        while i <= j:
            
            if people[i] + people[j] <= limit:
                i+=1
                j-=1
                
            else:
                j-=1
                
            ans+=1
            
        return ans
        
