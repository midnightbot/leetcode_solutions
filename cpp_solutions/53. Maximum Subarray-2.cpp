//ss
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int sum = 0;
        int ans = nums[0];
        
        for(int x:nums){
            sum+=x;
            if (sum < 0){
                ans = max(ans, sum);
                sum = 0;
            }else{
                ans = max(ans, sum);
            }
        }
        return ans;
        
    }
};
