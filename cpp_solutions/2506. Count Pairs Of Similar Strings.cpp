class Solution {
public:
    string map_this(string word){
        vector<int> temp(26,0);
        for(auto it : word){
            temp[int(it) - int('a')]+=1;
        }
        string key = "";
        for(int i=0;i<temp.size();++i){
            if (temp[i]!=0){
                key+=to_string(i);
                key+=",";
            }
        }
        return key;
        
    }
    int similarPairs(vector<string>& words) {
        map<string, int> maps;
        for(auto it : words){
            string ans = map_this(it);
            if(maps.find(ans)!=maps.end()) {
                maps[ans]+=1;
            } else{
                maps.insert({ans, 1});
            }
        }
        int res = 0;
        for(auto it : maps) {
            int n = it.second;
            res+= (n) * (n-1) / 2;
            // cout << it.first << "  "<<it.second << "\n";
        }
        return res;
        
    }
};
