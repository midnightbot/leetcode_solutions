class Solution {
public:
    vector<int> intersection(vector<vector<int>>& nums) {
        
        unordered_set<int> seen;
        
        for(int x:nums[0]){
            seen.insert(x);
        }
        
        unordered_set<int> temp;
        
        for(int x=1;x<nums.size();x++){
            for(int y: nums[x]){
                if(seen.find(y)!= seen.end()){
                    temp.insert(y);
                }
            }
            seen = temp;
            temp.clear();
        }
        
        
        //set to vector conversion
        vector<int> ans;
        for(int x: seen){
            ans.push_back(x);
        }
        sort(ans.begin(),ans.end());
        return ans;
        
    }
};
