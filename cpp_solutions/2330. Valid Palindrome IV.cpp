//sss
class Solution {
public:
    bool makePalindrome(string s) {
        int change = 0;
        int n = s.length();
        
        for(int x=0; x<floor(n/2);++x) {
            if (s[x]!=s[n-1-x]) {
                change++;
            }
            
        }
        return change<=2;
        
    }
};
