class Solution {
public:
    int percentageLetter(string s, char letter) {
        int count = 0;
        
        for(char ch: s){
            if (ch == letter){
                count+=1;
            }
        }
        return (int) count*100/s.length();
        
    }
};
