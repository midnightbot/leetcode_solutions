class Solution {
public:
    bool findSubarrays(vector<int>& nums) {
        set<int> seen;
        for(int x =0; x<nums.size()-1; ++x) {
            int temp = nums[x] + nums[x+1];
            if (seen.find(temp)!=seen.end()) {
                return true;
            } else {
                seen.insert(temp);
            }
        }
        return false;
    }
};
