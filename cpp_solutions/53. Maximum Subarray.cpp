//ss
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int ans = nums[0];
        int temp_ans = nums[0];
        
        for(int x=1;x<nums.size();x++){
            temp_ans = max(nums[x], temp_ans + nums[x]);
            ans = max(ans, temp_ans);
        }
        return ans;
        
    }
};
