##ss
##simple recursion
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        ##no two consecutive integers together
        
        
        ans = set()
    
        def form(pointer,curr,last_int):
            #print(pointer,curr,last_int)
            if pointer == len(word):
                ans.add(curr)
            elif curr == "":
                newcurr = word[pointer]
                newcurr2 = "1"
                #print(newcurr,newcurr2)
                form(pointer+1,newcurr,-1)
                form(pointer+1,newcurr2,1)
                
            elif pointer < len(word):
                
                if last_int == -1:
                    newc = copy.copy(curr)
                    newc+="1"
                    
                    newc2 = copy.copy(curr)
                    newc2+=word[pointer]
                    form(pointer+1,newc,1)
                    form(pointer+1,newc2,-1)
                    
                    
                else:
                    newc = copy.copy(curr)
                    ints = last_int + 1
                    ints = str(ints)
                    lens = len(ints)
                    newc = newc[0:len(newc)-len(str(last_int))] + ints
                    
                    newc2 = copy.copy(curr)
                    newc2+=word[pointer]
                    
                    form(pointer+1,newc,int(ints))
                    form(pointer+1,newc2,-1)
        form(0,"",-1)
        #print("11" in ans)
        return ans
    
        
