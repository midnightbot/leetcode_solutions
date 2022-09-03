class Solution {
public:
    set<int> seen;
    vector<int> result;
    map<int, vector<int>> graph;
    // Prints the Map
    void PrintMap(map<int, vector<int>> g) {
        for(auto it : g) {
            cout << it.first << "--";
            for(auto its : it.second) {
                cout << its << " ";
            }
            cout << "\n";
        }
    }
    // Converts vector<int> to int
    // {1,2,3} => 123
    int get_num(vector<int> arr) {
        int total = 0;
        int dec = 1;
        reverse(arr.begin(), arr.end());
        for(auto it : arr) {
            total+= it * dec;
            dec*=10;
        }
        return total;
    }
    // Recursive function to solve the problem
    // using dfs
    void find_ans(vector<int> arr, int pos) {
        if (pos == arr.size()) {
            int this_ans = get_num(arr);
            if (seen.find(this_ans)==seen.end()) {
                seen.insert(this_ans);
                result.emplace_back(this_ans);
            }
        } else {
            if (graph[arr[pos-1]].size()!=0) {
                for (auto it : graph[arr[pos-1]]) {
                    arr[pos] = it;
                    find_ans(arr, pos+1);
                }
            }
        }
    }
    vector<int> numsSameConsecDiff(int n, int k) {
        
        seen.clear();  // clearing every run
        result.clear();  // clearing every run
        graph.clear();  // clearing every run 
        vector<int> emp;
        for(int x=1 ; x<=9; ++x) {
            graph.insert({x,emp});
        }
        // finding all the neighbours for all digits
        for(int x=0; x<=9; ++x) {
            if (x+k < 10) {
                graph[x].emplace_back(x+k);
            }
            if (x-k >=0) {
                graph[x].emplace_back(x-k);
            } 
        } 
        
        vector<int> final_ans(n,-1);
        for(int x=1; x<=9; ++x) {
            final_ans[0] = x;
            find_ans(final_ans, 1);
        }
        // PrintMap(graph);
        return result;
    }
};
