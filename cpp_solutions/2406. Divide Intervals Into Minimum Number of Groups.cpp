class Solution {
public:
    // Simple Line Sweep Algorithm
    void PrintMap(map<float, int> arr) {
        
        for (auto it : arr){
            cout << it.first << "--" << it.second << "\n";
        }
    }
    
    void PrintVec(vector<vector<float>> arr) {
        
        for (auto it : arr){
            for(auto its : it) {
                cout << its << "--";
            }
            cout << "\n";
        }
    }
    
    int minGroups(vector<vector<int>>& intervals) {
        
        map<float, int> dicts;
        
        for(auto it : intervals) {
            float a = it[0] - 0.01;
            if (dicts.find(a)!=dicts.end()) {
                dicts[a]+=1;
            }  else {
                dicts[a] = 1;
            }
            
            
            float b = float(it[1]);
            if (dicts.find(b)!=dicts.end()) {
                dicts[b]-=1;
            }  else {
                dicts[b] = -1;
            }
        }
        
        
        vector<vector<float>> arr;
        
        for (auto it : dicts) {
            vector<float> temp;
            temp.emplace_back(it.first);
            temp.emplace_back(it.second);
            arr.emplace_back(temp);
        }
        
        // PrintVec(arr);
        sort(arr.begin(), arr.end());
        // PrintVec(arr);
        int curr = 0;
        int ans = 0;
        
        for(auto it : arr) {
            curr+= int(it[1]);
            ans = max(ans, curr);
        }
        return ans;
    }
};
