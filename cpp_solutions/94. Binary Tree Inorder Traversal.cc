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

// left  root  right
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == nullptr) {
            return {};
        } else {
            vector<int> l = inorderTraversal(root->left);
            vector<int> r = inorderTraversal(root->right);
            
            l.emplace_back(root->val);
            l.insert(l.end(), r.begin(), r.end());
            return l;
        }
    }
};
