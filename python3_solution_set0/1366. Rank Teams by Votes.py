##ss
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        
        ## compare all ranks for all team
        
        
        position = len(votes[0])
        
        temp = [0 for x in range(position)]
        
        dicts = {}
        
        for z in range(len(votes[0])):
            dicts[votes[0][z]] = [0 for x in range(position)]
            
        #print(dicts)
        for x in range(len(votes)):
            for y in range(len(votes[0])):
                #print(dicts[votes[x][y]][y])
                dicts[votes[x][y]][y]+=1
                #print(dicts)
            #print(dicts)
        #print(dicts)
        
        compare = []
        for x in dicts.keys():
            temp = []
            temp = dicts[x]
            temp.append(x)
            
            compare.append(temp)
            
        compare = sorted(compare, reverse = True, key = lambda x:(x[0:len(compare[0])-1],-ord(x[len(compare[0])-1])))
        
        ans = ""
        
        for x in range(len(compare)):
            ans+=compare[x][len(compare[0])-1]
            
        return ans
            
