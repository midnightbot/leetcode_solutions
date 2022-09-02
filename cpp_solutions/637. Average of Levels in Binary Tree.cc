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
    void DoPrint(vector<vector<long long int>> arr) {
        for(auto it : arr) {
            for (auto its : it) {
                cout << its << " ";
            }
            cout << "\n";
        }
    }
    double find_avg(vector<long long int> arr) {
        long long int temp = 0;
        for(auto it : arr) {
            temp+=it;
        }
        return temp / (double) arr.size();
        
    }
    vector<double> averageOfLevels(TreeNode* root) {
        vector<vector<long long int>> lvls;
        vector<TreeNode*> q;
        q.emplace_back(root);
    
        
        while (!q.empty()) {
            vector<TreeNode*> new_q;
            vector<long long int> this_lvl;
            for(auto it : q) {
                this_lvl.emplace_back(it->val);
                if (it->left!=nullptr) {
                    new_q.emplace_back(it->left);
                }
                if (it->right!=nullptr) {
                    new_q.emplace_back(it->right);
                }
            }
            q = new_q;
            lvls.emplace_back(this_lvl);
        }
        // DoPrint(lvls);
        vector<double> ans;
        for(auto it : lvls) {
            ans.emplace_back(find_avg(it));
        }
        return ans;
    }
};
