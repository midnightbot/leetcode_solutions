class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        int ans = 0;
        
        //cout << (3 & 5);
        
        for(int x = 1; x<=10000000; x <<= 1){
            int temp = 0;
            for(int y = 0; y < candidates.size();y++){
                
                if (x & candidates[y]){
                    temp++;
                }
            }
            ans = max(ans, temp);
        }
        
        return ans;
        
    }
};
