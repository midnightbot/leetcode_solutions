class Solution {
public:
    void print_vec(vector<int> arr){
        for(auto it : arr){
            cout << it << " ";
        }
    }
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> fac(n,0);
        vector<int> out(n,0);
        // print_vec(fac);
        for(auto it : trust){
            int a = it[0];
            int b = it[1];

            fac[b-1]+=1;
            out[a-1]+=1;
        }
        // print_vec(fac);
        for(int x=0; x<n; ++x){
            if (fac[x] == n-1 && out[x] == 0){
                return x+1;
            }
        }
        return -1;
    }
};
