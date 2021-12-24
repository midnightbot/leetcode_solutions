##ss
class Solution:
    def originalDigits(self, s: str) -> str:
        
        dicts = {}
        for x in range(26):
            dicts[chr(97+x)] = 0
            
        freq = [0 for x in range(10)] 
        
        for x in range(len(s)):
            dicts[s[x]]+=1

        ##zero one two three four five six seven eight nine       
        ## unique  - zero two four six eight
        ## z w u x g 
        ## o is in zero and one
        ##
        #print(dicts)
        
        #[0,2,3,4,5,6,7,8,9]
        freq[0] = dicts['z']


        freq[2] = dicts['w']


        freq[4] = dicts['u']


        freq[6] = dicts['x']


        freq[8] = dicts['g']
        
        freq[3] = dicts['h'] - freq[8]
        
        freq[5] = dicts['f'] - freq[4]
        
        freq[7] = dicts['s'] - freq[6]
        
        freq[9] = dicts['i'] - freq[5] - freq[6] - freq[8]
        
        freq[1] = dicts['o'] - freq[0] - freq[2] - freq[4] 
        

        ans = ""
        for x in range(len(freq)):
            for y in range(freq[x]):
                ans+=str(x)
                
        return ans
            
            
        
        
