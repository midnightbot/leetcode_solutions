##ss
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        
        pos = {'a':[0,0],'b':[0,1],'c':[0,2],'d':[0,3],'e':[0,4], 'f':[1,0],'g':[1,1],'h':[1,2],'i':[1,3],'j':[1,4],'k':[2,0],'l':[2,1],'m':[2,2],'n':[2,3],'o':[2,4],'p':[3,0],'q':[3,1],'r':[3,2],'s':[3,3],'t':[3,4],'u':[4,0],'v':[4,1],'w':[4,2],'x':[4,3],'y':[4,4],'z':[5,0]}
        #print(pos)
        #print(pos['e'])
        curr_pos = [0,0]
        
        result = ""
        
        for x in range(len(target)):
            #print(result)
            result+= self.give_path(curr_pos,pos[target[x]]) + "!"
            curr_pos = pos[target[x]]
            
        return result
        
    def give_path(self,p1,p2):
        ##we have to go from p1 -> p2
        if (p1!=[5,0] and p2!=[5,0]) or (p1 == p2):
            ans = ""
            if p1[0] > p2[0]:
                diff = p1[0] - p2[0]
                for x in range(diff):
                    ans+="U"

            else:
                diff = p2[0] - p1[0]
                for x in range(diff):
                    ans+='D'


            if p1[1] > p2[1]:
                diff = p1[1] - p2[1]
                for x in range(diff):
                    ans+='L'

            else:
                diff = p2[1] - p1[1]
                for x in range(diff):
                    ans+="R"
            return ans
        elif p1 == [5,0]:
            ans = ""
            diff = p1[0] - p2[0]
            for x in range(diff):
                ans+='U'
                
            diff = p2[1] - p1[1]
            for x in range(diff):
                ans+="R"
                
            return ans
        
        elif p2 == [5,0]:
            ans = ""
            diff = p1[1] - p2[1]
            for x in range(diff):
                ans+="L"
                
            diff = p2[0] - p1[0]
            
            for x in range(diff):
                ans+="D"
                
            return ans
        
