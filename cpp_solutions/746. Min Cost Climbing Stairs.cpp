class Solution {
public:
    unordered_map<int, int> memo;
    int minCostClimbingStairs(vector<int>& cost) {
        return find_ans(cost, cost.size());
        
        
    }
    
    int find_ans(vector<int>& cost,int n){
        if (n==0 || n==1){
            return 0;
        }
        else if (memo.find(n)!=memo.end()){
            return memo[n];
        }
        else{
            int a = cost[n-1] + find_ans(cost, n-1);
            int b = cost[n-2] + find_ans(cost, n-2);
            
            if (a < b){
                memo[n] = a;
                
            }
            else{
                memo[n] = b;
            }
            
            return memo[n];
        }
    }
};
