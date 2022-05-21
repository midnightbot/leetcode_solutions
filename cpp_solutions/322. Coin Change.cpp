class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        
        int inf_max = amount + 1;
        
        vector<int> dp(amount+1,inf_max);
        
        dp[0] = 0;
        
        for(int x=1; x<=amount;x++){
            for(int y=0 ; y<coins.size();y++){
                if(coins[y] <= x){
                    dp[x] = min(dp[x],1+dp[x-coins[y]]);
                }
                
            }
        }
        
        if (dp[amount]!=amount+1){
            return dp[amount];
        }
        else{
            return -1;
        }
    }
};
