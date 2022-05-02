class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        
        int n = prices.size();
        
        if (n < 2){
            return 0;
        }
        int temp = prices[0];
        int profit = 0;
        for (int p:prices){
            if (p < temp){
                temp = p;
            }
            else if(p > temp + fee){
                profit+= p - temp - fee;
                temp = p - fee;
            }
        }
        return profit;
        
    }
};
