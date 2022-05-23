//ss
class Solution {
public:
    int countPrefixes(vector<string>& words, string s) {
        
        int ans = 0;
        
        for (string comp: words){
            if (isprefix(comp,s)){
                ans+=1;
            }
        }
        return ans;
        
        
    }
    bool isprefix(string s1, string s2){
        //s1 is array string 
        //s2 is the given string
        
        if (s1.length() > s2.length()){
            return false;
        }
        else{
            for(int x=0;x<s1.length();x++){
                if (s1.at(x)!=s2.at(x)){
                    return false;
                }
            }
            return true;
        }
    }
};
