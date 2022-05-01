class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        
        // values[i] + i -> a
        
        // values[j] - j -> b
        // i < j
        // maximize a+b
        
        int n = values.size();
        vector<int> temp(n,0);
        temp[n-1] = values[n-1] - (n-1); // this is values[i] - i array
            
        for (int x=values.size()-2;x>=0;x--){
            temp[x] = max(temp[x+1], values[x] - (x));
        }
        
        int ans = 0;
        
        for(int x=0; x<values.size()-1;x++){
            ans = max(ans, values[x]+x + temp[x+1]);
        }
        
        
        return ans;
        
    }
};
