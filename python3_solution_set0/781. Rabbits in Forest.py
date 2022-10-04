##ss
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        answers = sorted(answers)
        
        dicts = {}
        
        count = 0
        
        for x in range(len(answers)):
            if answers[x] == 0: ## if rabbit answers 0, he is unique, add it to count
                count+=1
            elif answers[x]!=0 and answers[x] in dicts.keys():
                dicts[answers[x]]+=1
                
            elif answers[x]!=0 and answers[x] not in dicts.keys():
                dicts[answers[x]] = 1
                
             
        
       
        ##dicts[x] give number of rabbits that have same answer x
        for x in dicts.keys():
            #print(count)
            fac = dicts[x] % (x+1) ## number of rabbits not in complete group
            quo = dicts[x] // (x+1) ##number of complete groups that can be formed
            ##example if 5 rabbits answer 3
            
            ## 4 rabbits can be of same color
            ##rabbit1 red says three more of red color (rabbit2,rabbit3,rabbit4)
            ##rabbit2 red says three more of red color (rabbit1,rabbit3,rabbit4)
            ##rabbit3 red says three more of red color (rabbit1,rabbit2,rabbit4)
            ##rabbit4 red three more of red color (rabbit1,rabbit2,rabbit3)
            ##rabbit5 cannot be of red color, say it is green and says 3 more of green color
            ## 1 rabbit of different color
            
            count+= (quo) * (x+1)  ## (no. of complete groups) * (size of group)
            if fac!=0:
                count+=(x+1) ##if some rabbits not in complete group, just add group size once
           
        return count
