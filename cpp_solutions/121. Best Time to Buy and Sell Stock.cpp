class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int ans = 0;
        int mins = prices[0];
        
        for (int x = 0; x < prices.size();x++){
            mins = min(mins,prices[x]);
            ans = max(ans, prices[x] - mins);
        }
        
        return ans;
    }
};
