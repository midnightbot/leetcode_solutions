class Solution {
public:
    int matrixMedian(vector<vector<int>>& grid) {
        int ans = 0;
        vector<int> arr;
        for(auto it : grid) {
            for(auto its : it) {
                arr.push_back(its);
            }
        }
        int n = (int) arr.size()/2;
        sort(arr.begin(),arr.end());
        return arr[n];
    }
};
