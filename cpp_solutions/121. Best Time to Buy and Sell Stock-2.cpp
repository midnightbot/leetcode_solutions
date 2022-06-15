//ss
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int n = prices.size();
        vector<int> maxs(n,0);
        
        int curr = prices[n-1];
        for(int x=n-2; x>=0;x--){
            maxs[x] = curr;
            curr = max(curr, prices[x]);
        }
        
        /*
        for (auto& it: maxs){
            cout << it << "\n";
        }
        */
        int ans = 0;
        
        for(int x=0; x< n; x++){
            ans = max(ans, maxs[x] - prices[x]);
        }
        return ans;
        
    }
};
