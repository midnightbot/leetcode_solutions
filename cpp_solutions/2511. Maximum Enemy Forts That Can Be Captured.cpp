class Solution {
public:
    int captureForts(vector<int>& forts) {

        int ans = 0;
        int j = 0;
        for(int i=0; i<forts.size();++i){
            if (forts[i]!=0){
                if(forts[j] == -forts[i]){
                    ans = max(ans, i-j-1);
                }
                j = i;
            }
        }
        return ans;
    }
};
