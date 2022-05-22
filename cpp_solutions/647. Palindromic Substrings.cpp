class Solution {
public:
    int countSubstrings(string s) {
        int count = 0;
        int n = s.length();
        
        vector<vector<bool>> dp(n,vector<bool>(n,false));
        
        for(int x=0; x<n;x++){
            dp[x][x] = true;
            count+=1;
        }
        
        for(int x=n-1;x>=0;x--){
            for(int y=x+1;y<n;y++){
                if(s.at(x) == s.at(y) && ((y-x==1) || dp[x+1][y-1])){
                    dp[x][y] = true;
                    count+=1;
                }
            }
        }
        
        return count;
        
    }
};
