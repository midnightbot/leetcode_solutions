class Solution {
public:
    int numTrees(int n) {
        
        vector <int> dp(n+1,0);
        
        if (n==1){
            return 1;
        }
        else if(n == 2){
            return 2;
        }
        else if(n == 3){
            return 5;
        }
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 5;
        
        for(int x = 4; x < n+1 ; x++){
            for (int y = 1 ; y < x+1 ; y++){
                dp[x]+=dp[y-1] * dp[x-y];
            }
        }
        
        return dp[n];
    }
};
