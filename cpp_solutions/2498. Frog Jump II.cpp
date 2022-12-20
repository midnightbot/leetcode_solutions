class Solution {
public:
    int maxJump(vector<int>& stones) {
        if (stones.size() == 2){
            return stones[1] - stones[0];
        } else {
            int ans = -1;
            for (int x=0; x<stones.size()-2;++x){
                ans = max(ans, stones[x+2] - stones[x]);
            }
            return ans;
        }
        
    }
};
