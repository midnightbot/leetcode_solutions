class Solution {
public:
    long long countSubarrays(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n,1);
        for(int x =1 ; x < n ; ++x) {
            if (nums[x] > nums[x-1]) {
                dp[x] = 1 + dp[x-1];
            } 
        }
        long long ans = accumulate(dp.begin(), dp.end(), 0LL);
        return ans;
    }
};
