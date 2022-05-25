class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        
        int n = envelopes.size();
        sort(envelopes.begin(),envelopes.end());
        vector<int> dp(n,1);
        
        for(int x=1;x<n;x++){
            for(int y=0;y<x;y++){
                if (envelopes[x][0] > envelopes[y][0] && envelopes[x][1] > envelopes[y][1]){
                    dp[x] = max(dp[x], 1 + dp[y]);
                  
                }
            }
        }
        
        return *std::max_element(dp.begin(),dp.end());
        
        
    }
};
