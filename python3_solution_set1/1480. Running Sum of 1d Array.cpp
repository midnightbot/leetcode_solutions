class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        
        vector<int> ans;
        int still = 0;
        
        for(int x=0;x<nums.size();x++){
            still+= nums[x];
            ans.push_back(still);
        }
        
        return ans;
        
    }
};
