/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void printset(set<int> arrs) {
        for (auto it : arrs) {
            cout << it << " ";
        }
        cout << "\n";
    }
    int amountOfTime(TreeNode* root, int start) {
        
        int node_count = 0;
        vector<pair<int,int>> edges;
        map<int,vector<int>> g;
        queue<TreeNode> q;
        q.push(*root);
        // finding all the edges in the tree
        while (!q.empty()) {
            ++node_count;
            TreeNode top = q.front();            
            q.pop();
            if (top.left!=nullptr) {
                q.push(*top.left);
                pair<int,int> new_pair;
                new_pair.first = top.val;
                new_pair.second = top.left->val;
                edges.emplace_back(new_pair);
            }
            if (top.right!=nullptr) {
                q.push(*top.right);
                pair<int,int> new_pair;
                new_pair.first = top.val;
                new_pair.second = top.right->val;
                edges.emplace_back(new_pair);
            }
            
        }
        
        // making the graph
        for (auto it : edges) {
            if (g.find(it.first)!=g.end()) {
                g[it.first].emplace_back(it.second);
            } else {
                vector<int> temp;
                temp.emplace_back(it.second);
                g[it.first] = temp;
            }
            
            if (g.find(it.second)!=g.end()) {
                g[it.second].emplace_back(it.first);
            } else {
                vector<int> temp;
                temp.emplace_back(it.first);
                g[it.second] = temp;
            }
        }
        //
        int seen = 1;
        int mins = 0;
        set<int> visited;
        queue<int> qs;
        qs.push(start);
        while (seen!=node_count) {
            ++mins;
            int rangs = qs.size();
            for(int x =0; x<rangs;++x) {
                int curr_node = qs.front();
                qs.pop();
                if (visited.find(curr_node) == visited.end()) {
                    visited.insert(curr_node);
                    for(auto nei : g[curr_node]) {
                        if (visited.find(nei) == visited.end()) {
                            ++seen;
                            qs.push(nei);
                        }
                    }
                }
            }
            // printset(visited);
            
        }
        // printset(visited);
        cout << node_count;
        return mins;   
    }
    
};
