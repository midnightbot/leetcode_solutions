class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obs) {
        
        int m = obs.size();
        int n = obs[0].size();
        
        int dp[100][100] = {0};
        
        for (int x =0 ; x< m ; x++){
            if (obs[x][0] == 1){
                break;
            }
            else{
                dp[x][0] = 1;
            }
        }
        
        for(int x=0; x< n; x++){
            if(obs[0][x] == 1){
                break;
            }
            else{
                dp[0][x] = 1;
            }
        }
        
        for (int x=1 ; x<m; x++){
            for (int y=1; y<n;y++){
                if (obs[x][y]!=1){
                    dp[x][y] = dp[x-1][y] + dp[x][y-1];
                }
            }
        }
        return dp[m-1][n-1];
        //cout << obs[0].size();
        
        //return 0;
    }
};
