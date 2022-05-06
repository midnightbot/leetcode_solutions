class Solution {
public:
    string removeDuplicates(string s, int k) {
        
        vector<pair<char,short>> comp;
        
        for(int x=0; x< s.length();x++){
            if(comp.empty() || comp.back().first!=s[x]){
                comp.push_back({s[x],1});
            }
            else if(++comp.back().second == k){
                comp.pop_back();
            }
        }
        string result;
        
        for(int x=0; x<comp.size();x++){
            //cout << comp[x].first << comp[x].second;
            for(int cnt = 0; cnt < comp[x].second;cnt++){
                result+=comp[x].first;
            }
        }
        
        return result;
        
    }
};
