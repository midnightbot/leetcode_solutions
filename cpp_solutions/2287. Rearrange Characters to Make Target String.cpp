//ss
#include<cmath>
using namespace std;
class Solution {
public:
    int rearrangeCharacters(string s, string target) {
        
        vector<int> big;
        vector<int> small;
        
        big = mapper(s);
        small = mapper(target);
        
        int result = 1000;
        
        for (int x=0;x<26;x++){
            if (small[x]!=0){
                result = min(result, (int)(big[x]/small[x]));
            }
        }
        
        return result;
        
    }
    
    vector<int> mapper(string s){
        vector<int> freq(26,0);
        
        for (char ch:s){
            freq[ch - 'a']+=1;
        }
        return freq;
    }
};
