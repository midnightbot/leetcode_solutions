class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int ans = 0;
        
        int curr = prices[0];
        
        for (int x=0;x<prices.size();x++){
            
            if (prices[x] < curr){
                curr = prices[x];
            }
            else{
                ans+= prices[x] - curr;
                curr = prices[x];
            }
        }
        return ans;
        
    }
};
