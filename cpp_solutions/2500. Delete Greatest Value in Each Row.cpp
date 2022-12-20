class Solution {
public:
    void print_vec(vector<vector<int>> & arr){

        for(auto it : arr){
            for(auto its : it) {
                cout << its << " ";
            }
            cout << "\n";
        }
    }
    int deleteGreatestValue(vector<vector<int>>& grid) {
        int size = grid[0].size();
        int vecs = grid.size();
        for(int x=0; x<vecs;++x){
            sort(grid[x].begin(), grid[x].end());
        }
        int ans = 0;
        // print_vec(grid);
        for(int x=0; x<size;++x){
            int maxs = -1;
            for(int y=0; y<vecs;++y){
                maxs = max(maxs, grid[y][x]);
            }
            ans+=maxs;
        }
        return ans;
    }
};
