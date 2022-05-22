//ss
class Solution {
public:
    int lengthOfLastWord(string s) {
        
        //cout << int(' ');
        int prev_count = 0;
        int last_seen = 0;
        for(char ch: s){
            if (int(ch)!=int(' ')){
                prev_count+=1;
            }
            else{
                if (prev_count > 0){
                   last_seen = prev_count; 
                }
                
                prev_count = 0;
            }
        }
        if (prev_count!=0){
            return prev_count;
        }
        return last_seen;
        
    }
};
