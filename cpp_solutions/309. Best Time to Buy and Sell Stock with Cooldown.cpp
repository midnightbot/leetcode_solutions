class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int n = prices.size();
        vector<int> dp(n+2,0);
        
        
        for (int i=n-1;i>=0;i--){
            
            for(int j= i+1;j < n;j++){
                dp[i] = max(dp[i],max(dp[i+1], prices[j]-prices[i] + dp[j+2]));
            }
            
        }
        return dp[0];
    
        
    }
};
