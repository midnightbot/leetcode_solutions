class Solution {
public:
    int jump(vector<int>& nums) {
        
        int n = nums.size();
        
        vector<int> dp(n,100000);
        dp[n-1] = 0;
        
        for (int x=n-2;x>=0;x--){
            int mins = 100000;
            for(int y=x;y<min(x+nums[x]+1,n);y++){
                if (dp[y] < mins){
                    mins = 1 + dp[y];
                }
            }
            dp[x] = mins;
        }
        
        return dp[0];
    }
};
