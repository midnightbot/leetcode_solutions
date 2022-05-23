class Solution {
public:
    vector<int> fullBloomFlowers(vector<vector<int>>& flowers, vector<int>& persons) {
        
        vector<int> fstart,fend;
        vector<int> ans;
        for(auto& it: flowers){
            fstart.push_back(it[0]);
            fend.push_back(it[1]);
        }
        
        sort(fstart.begin(),fstart.end());
        sort(fend.begin(),fend.end());
        
        for(int it: persons){
            int starttime = upper_bound(fstart.begin(),fstart.end(),it) - fstart.begin(); //bisect_right
            int endtime = lower_bound(fend.begin(),fend.end(),it) - fend.begin(); // bisect_left
            ans.push_back(starttime - endtime);
            
            
        }
        return ans;
        
    }
};
