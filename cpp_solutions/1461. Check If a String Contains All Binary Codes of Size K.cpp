class Solution {
public:
    bool hasAllCodes(string s, int k) {
        unordered_set<string> temp;
        
        if (k > s.size()){
            return false;
        }
        for(int x=0;x<s.length()-k+1;x++){
            temp.insert(s.substr(x,k));
        }
        
        return temp.size() == pow(2,k);
        
    }
};
