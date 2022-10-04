##ss
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        ##always try to find the position of the next smallest person
        
        ans = [[] for x in range(len(people))]
        
        people = sorted(people, key = lambda x:(x[0],x[1]))
        #print(people)
        
        for x in range(len(people)):
            count = 0
            for y in range(len(people)): ##if a position is empty, the next inserted person there will always have height greater than or equal to the current person
                if count == people[x][1]:
                    break
                if len(ans[y]) == 0 or ans[y][0]>=people[x][0]:
                    count+=1
                    
            for z in range(y,len(ans)):
                if len(ans[z]) == 0:
                    ans[z] = people[x]
                    break
                    
        return ans
            
