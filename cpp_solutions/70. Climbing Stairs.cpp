class Solution {
public:
    unordered_map<int,int> memo;
    int climbStairs(int n) {
        if (n == 0 || n==1){
            return 1;
        }
        else if (memo.find(n)!=memo.end()){
            return memo[n];
        }
        else{
            memo[n] = climbStairs(n-1) + climbStairs(n-2);
            return memo[n];
        }
    }
};
