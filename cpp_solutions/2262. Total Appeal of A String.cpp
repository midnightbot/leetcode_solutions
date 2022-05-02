//ss
class Solution {
public:
    long long appealSum(string s) {
        int n = s.size();
        
        vector<int> dp(n+1,0);
        
        vector<int> prev(26,-1);
        dp[0] = 1;
        prev[int(s[0]) - int('a')] = 0;
            
        for (int x=1;x<n;x++){
            //cout << s[x] << int(s[x]) << prev[0] ;
            
            dp[x] = dp[x-1] + x  - prev[int(s[x])-int('a')];
            //cout << dp[x] << "--" << dp[x-1] << int(s[x])-int('a');
            prev[int(s[x])-int('a')] = x;
            
        }
     
        long long ans = 0;
        for (int x=0;x<dp.size();x++){
            ans+=dp[x];
            //cout << dp[x] << "\n";
            //cout << ans;
        }
        return ans;
    }
};
